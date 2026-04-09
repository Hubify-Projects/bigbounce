# Hubify Labs — macOS Desktop App Spec

**Status:** SPEC IN PROGRESS · category C of `BUILD_READINESS_CHECKLIST.md`
**Author:** Houston Golden + Claude
**Date locked:** 2026-04-08
**Linked from:** PRD §42 (placeholder · TBD), `BUILD_READINESS_CHECKLIST.md` Category C

---

## 0. The premise

The macOS desktop app is **a Tauri 2.x shell wrapping the same React/Convex web app** that runs at `hubify-labs.com`. 95% of the functionality is identical to web. The app exists for the 5% that needs native integration: dock badge, system notifications, native file drop, `hubify://` URL scheme handler, launchd background service for the orchestrator, and the menu bar app variant.

**Decision: Tauri 2 over Electron over native Swift.** Tauri gives us:
- 5-10x smaller bundle than Electron (~10MB vs ~100MB)
- Native macOS feel via WKWebView (Apple's web engine, not Chromium)
- Rust backend for fast file system + system integration
- Same webview as Safari → no separate browser to update
- Code signing + notarization is well-trodden territory

**Why not native Swift:** writing the entire app twice (web + Swift) is too much work for a 1-person team. Tauri gives us the shell + the native bridges we need without doubling the codebase.

**Why not Electron:** bundle size + memory footprint. Houston runs the platform on a MacBook — every MB matters.

---

## 1. The native features (the 5% Tauri unlocks)

Everything else (the chat, the mockup, the sidepeek system, the cosmic orb, the activity graph, the file preview, the agent system) is the existing web app loaded into a Tauri webview. These are the things that DON'T work on web:

### 1.1 Native window chrome

**Decision: borderless window** like Linear and Cursor (not the standard macOS title bar). Reasons:
- The platform's UI is dense and pixel-precious — every 22px of title bar saved is 22px more for content
- The custom title bar lets us put the Director header pill (`$29.35 · 47h runway`) and the cosmic orb status indicator at the very top of the window
- macOS traffic lights (close / minimize / maximize) get rendered as overlay buttons in the top-left, native macOS style
- Drag-region is the entire top 28px of the window (can drag from any non-button area)

Implementation:
```rust
// src-tauri/tauri.conf.json
{
  "tauri": {
    "windows": [{
      "title": "Hubify Labs",
      "width": 1440,
      "height": 900,
      "decorations": false,           // borderless
      "transparent": false,
      "titleBarStyle": "Overlay",     // native traffic lights as overlay
      "hiddenTitle": true,
      "minWidth": 720,
      "minHeight": 480
    }]
  }
}
```

### 1.2 Native menu bar (the App / File / Edit / View / Window / Help menu)

```
Hubify Labs              File              Edit              View              Window              Help
─────────────            ──────            ──────            ──────            ────────            ──────
About Hubify Labs        New chat ⌘N       Cut ⌘X            Director ⌘1       Minimize ⌘M         Hubify Docs
Settings... ⌘,           New note ⌘⇧N      Copy ⌘C           Overview ⌘2       Zoom                Keyboard shortcuts ⌘?
─────────────            New experiment    Paste ⌘V          Experiments ⌘3    ────────            Report a bug
Hide ⌘H                  Open file... ⌘O   ────────          Papers ⌘4         Toggle full screen  ────────
Hide others ⌥⌘H          ────────          Find ⌘F           ...               ────────            View on GitHub
Show all                 Save ⌘S           Find next ⌘G      Show notifications ⌘⇧I   Bring all to front
─────────────            Save as... ⌘⇧S    ────────                              ────────
Quit ⌘Q                  ────────          Select all ⌘A                         Hubify Labs (1)
                         Print... ⌘P                                                Bigbounce Lab
                         ────────
                         Recent files ▶
```

Implementation: Tauri's `Menu::with_items()` API. Each menu item has:
- A `MenuItemAttributes::new(label).accelerator(shortcut)` definition
- An event handler that triggers a JS callback in the webview (`window.dispatchEvent(new CustomEvent('hubify:menu', { detail: 'new-note' }))`)
- The webview's React app listens for these events and routes them to the right action

### 1.3 Dock badge for unread notifications

When the Director has unread notifications (per the existing notifications drawer), the macOS dock icon shows a red badge with the count.

```rust
// src-tauri/src/main.rs
use tauri::api::notification::Notification;

#[tauri::command]
fn set_dock_badge(count: u32) -> Result<(), String> {
    #[cfg(target_os = "macos")]
    unsafe {
        use cocoa::base::nil;
        use cocoa::foundation::NSString;
        use objc::{msg_send, sel, sel_impl};

        let app: cocoa::base::id = msg_send![class!(NSApplication), sharedApplication];
        let dock_tile: cocoa::base::id = msg_send![app, dockTile];
        let label = if count == 0 { nil } else { NSString::alloc(nil).init_str(&count.to_string()) };
        let _: () = msg_send![dock_tile, setBadgeLabel: label];
    }
    Ok(())
}
```

The web app calls `invoke('set_dock_badge', { count: unreadCount })` whenever the unread count changes.

### 1.4 Native notifications (NSUserNotification)

When an agent fires a notification (e.g., "GPU IDLE" or "credits at $18.40"), the macOS Notification Center gets a real native notification, not just an in-app toast.

```rust
#[tauri::command]
fn show_notification(title: String, body: String, deeplink: Option<String>) -> Result<(), String> {
    Notification::new("com.hubifylabs.app")
        .title(&title)
        .body(&body)
        .show()
        .map_err(|e| e.to_string())?;
    // If a deeplink is provided, store it so the click handler can route to it
    if let Some(link) = deeplink {
        STORED_DEEPLINK.lock().unwrap().replace(link);
    }
    Ok(())
}
```

When the user clicks the notification, macOS brings the app to the foreground and the deeplink (a `hubify://...` URL) gets routed to the right view.

### 1.5 Native file drop (drag from Finder into the app)

Drag a file from Finder onto the Hubify Labs window → the app opens that file in the right pane (file preview tab) OR uploads it to the current chat (if the chat composer is focused).

```rust
// In tauri.conf.json:
"fileDropEnabled": true

// In React:
useEffect(() => {
  const unlisten = listen('tauri://file-drop', (event) => {
    const paths = event.payload as string[];
    // Route to the active surface
    if (chatComposerFocused) {
      attachFilesToChat(paths);
    } else {
      paths.forEach(p => openFilePreview(p));
    }
  });
  return () => { unlisten.then(fn => fn()); };
}, []);
```

### 1.6 The `hubify://` URL scheme handler (registered in Info.plist)

Per PRD §40.17 Tier 4. Examples:
- `hubify://chats/abc123` — open a chat
- `hubify://labs/bigbounce-hubify/projects/fnl-tracer-pipeline` — open a project
- `hubify://labs/bigbounce-hubify/files/arxiv/main.tex` — open a file
- `hubify://agents/bigbounce-orchestrator` — open the agent sidepeek

```xml
<!-- src-tauri/Info.plist -->
<key>CFBundleURLTypes</key>
<array>
  <dict>
    <key>CFBundleURLName</key>
    <string>com.hubifylabs.app</string>
    <key>CFBundleURLSchemes</key>
    <array>
      <string>hubify</string>
    </array>
  </dict>
</array>
```

Tauri's `tauri-plugin-deep-link` handles the rest:
```rust
tauri::Builder::default()
    .plugin(tauri_plugin_deep_link::init())
    .setup(|app| {
        app.deep_link().on_open_url(|event| {
            let url = event.urls()[0].as_str();
            // Forward to webview
            window.emit("hubify-deeplink", url).unwrap();
        });
        Ok(())
    })
```

The web app listens for `hubify-deeplink` events and routes them to the right view.

### 1.7 launchd background service for the orchestrator

The Hubify Labs orchestrator agent runs as a `launchd` background service so it stays alive even when the app window is closed. This is how the platform keeps standups firing, credits monitoring, and the autonomous polish loop running while Houston is sleeping or working in another app.

```xml
<!-- ~/Library/LaunchAgents/com.hubifylabs.orchestrator.plist -->
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.hubifylabs.orchestrator</string>
    <key>ProgramArguments</key>
    <array>
        <string>/Applications/Hubify Labs.app/Contents/MacOS/orchestrator</string>
        <string>--lab</string>
        <string>bigbounce-hubify</string>
    </array>
    <key>RunAtLoad</key>
    <true/>
    <key>KeepAlive</key>
    <true/>
    <key>StandardOutPath</key>
    <string>/tmp/hubify-orchestrator.log</string>
    <key>StandardErrorPath</key>
    <string>/tmp/hubify-orchestrator.err</string>
</dict>
</plist>
```

Loaded with `launchctl load ~/Library/LaunchAgents/com.hubifylabs.orchestrator.plist` on first install.

### 1.8 Native keyboard shortcuts

Globally registered shortcuts that work even when the app is in the background:

| Shortcut | Action |
|---|---|
| ⌘N | New chat |
| ⌘⇧N | New note |
| ⌘K / ⌘P | Open command palette |
| ⌘B | Toggle sidebar |
| ⌘J | Toggle chat |
| ⌘1-9 | Jump to view 1-9 (Director, Overview, Experiments, ...) |
| ⌘W | Close active file preview tab |
| ⌘⇧I | Toggle notifications drawer |
| ⌘, | Open Settings |
| ⌘⇧. | Toggle Director focus mode (full screen orchestrator chat) |
| ⌘? | Open keyboard shortcuts cheatsheet |

Implementation: Tauri's global shortcut plugin OR (for in-app only) the existing webview keyboard handlers from the existing mockup.

### 1.9 iCloud sync for journal notes (optional)

For Houston: an opt-in setting in `Settings → Sync` to enable iCloud sync of `lab/notes/` directories. Uses macOS native `NSFileCoordinator` + the `~/Library/Mobile Documents/iCloud~com~hubifylabs~app/` container.

```rust
fn enable_icloud_notes_sync(lab_slug: String) -> Result<(), String> {
    let icloud_dir = dirs::home_dir()
        .ok_or("no home dir")?
        .join("Library/Mobile Documents/iCloud~com~hubifylabs~app/notes")
        .join(&lab_slug);
    fs::create_dir_all(&icloud_dir).map_err(|e| e.to_string())?;
    // Symlink the lab's local notes dir to the iCloud container
    let local_notes = dirs::document_dir()
        .ok_or("no docs dir")?
        .join(format!("HubifyLabs/{}/notes", lab_slug));
    if !icloud_dir.read_link().is_ok() {
        std::os::unix::fs::symlink(&local_notes, &icloud_dir).map_err(|e| e.to_string())?;
    }
    Ok(())
}
```

This is OPTIONAL. Default is local-only. iCloud sync is for users who want to read their notes on iPhone (iOS app v2).

### 1.10 Code signing identity + notarization plan

Production builds require:
1. Apple Developer Program membership ($99/year) — Houston already has this
2. Developer ID Application certificate (for distribution outside the Mac App Store)
3. Notarization: every build is uploaded to Apple, scanned for malware, and stapled with a notarization ticket

Tauri's `tauri-action` GitHub Action handles signing + notarization in CI:
```yaml
# .github/workflows/release.yml
- uses: tauri-apps/tauri-action@v0
  env:
    APPLE_CERTIFICATE: ${{ secrets.APPLE_CERTIFICATE }}
    APPLE_CERTIFICATE_PASSWORD: ${{ secrets.APPLE_CERTIFICATE_PASSWORD }}
    APPLE_SIGNING_IDENTITY: ${{ secrets.APPLE_SIGNING_IDENTITY }}
    APPLE_ID: ${{ secrets.APPLE_ID }}
    APPLE_PASSWORD: ${{ secrets.APPLE_PASSWORD }}
    APPLE_TEAM_ID: ${{ secrets.APPLE_TEAM_ID }}
  with:
    tagName: v__VERSION__
    releaseName: 'Hubify Labs v__VERSION__'
```

### 1.11 Auto-update channel (Sparkle vs Tauri's built-in updater)

**Decision: Tauri's built-in updater** (`tauri-plugin-updater`).

Reasons:
- Tauri-native, no extra Sparkle integration needed
- Signed updates with Tauri's update key (separate from code signing)
- JSON manifest hosted at `https://updates.hubify-labs.com/macos/latest.json`
- Background check every 6 hours, prompt user to install on next quit

```rust
tauri::Builder::default()
    .plugin(tauri_plugin_updater::Builder::new().build())
    .setup(|app| {
        let handle = app.handle().clone();
        tauri::async_runtime::spawn(async move {
            let updater = handle.updater().unwrap();
            if let Ok(Some(update)) = updater.check().await {
                // Notify user, download, install on next quit
            }
        });
        Ok(())
    })
```

---

## 2. The menu bar app variant (the small icon in the macOS menu bar)

A second binary: `Hubify Labs Menu Bar` — a tiny always-resident app that lives in the macOS menu bar (the top-right system tray area). It's a separate process from the main app, much smaller, designed for users who want the platform always-watching but don't want a full window open.

### 2.1 What it shows (when you click the menu bar icon)

A dropdown popover (~340px wide) with:
- Director status: `● 3 agents active · last standup 13 min ago`
- Credits: `$29.35 · 47h runway` (color-coded per §41 thresholds)
- Quick chat input: a single-line text field that opens a `/chat` if you type something
- "Recent activity" — last 5 events from the activity feed
- "Open Hubify Labs" → opens the full app

### 2.2 Implementation

A second Tauri window with:
```json
{
  "label": "menubar",
  "url": "menubar.html",
  "decorations": false,
  "alwaysOnTop": true,
  "skipTaskbar": true,
  "focus": false,
  "width": 340,
  "height": 480,
  "visible": false
}
```

Toggled via `tauri-plugin-positioner` to anchor under the menu bar icon. Uses the macOS `NSStatusItem` API via Rust bindings to register the icon itself.

### 2.3 When to use the menu bar app

- Houston is doing other work (writing a paper in his editor, browsing arxiv) and wants to glance at lab status without switching apps
- He just wants to send a quick chat to the orchestrator without opening the full app
- He wants the credits/runway pill always visible in the system tray
- Low-touch monitoring without the cognitive overhead of a full app window

This is OPTIONAL. The full app always works without the menu bar variant.

---

## 3. The desktop mockup (visual layer)

Per `BUILD_READINESS_CHECKLIST.md` Category C item 3: build a separate `desktop-app-mockup.html` file that visually shows the macOS-specific chrome wrapping the existing web app.

### 3.1 What's in the desktop mockup

A single self-contained HTML file (similar pattern to `hubify-labs-mockups/index.html`) that renders:

1. **Native title bar** — borderless window with traffic lights (red/yellow/green dots) in the top-left, the Director credits pill in the top-center, and the cosmic orb status indicator + window controls in the top-right
2. **The full web app inside** — the existing mockup gets embedded as the body content
3. **Native menu bar visualization** — a faux macOS menu bar at the very top showing "Hubify Labs · File · Edit · View · Window · Help" with hover-state previews
4. **Dock indicator** — a small Hubify icon at the bottom of the screen with a red unread badge
5. **Native file drop overlay** — when the user (in the mockup) drags a file over the window, a sage-tinted overlay appears: "Drop to add to chat / open in preview pane"
6. **Notification preview** — a faux macOS notification banner sliding in from the top-right corner with a sample notification ("GPU IDLE — deploy next phase")
7. **Menu bar app preview** — a smaller window at the side showing the menu bar app variant's popover content

### 3.2 Why a separate mockup file (not extending index.html)

The web mockup is the canonical reference for the inside of the app. The desktop mockup is just the **outside frame** — the native chrome that wraps the same content. Keeping them separate means:
- The web mockup stays focused on flows and content
- The desktop mockup stays focused on native integration
- Future iOS / iPad mockups follow the same pattern (separate file per platform shell)

### 3.3 Status

- [ ] Build `desktop-app-mockup.html` (Category C item 3 in BUILD_READINESS_CHECKLIST.md)
- This is a future iteration of the autonomous loop

---

## 3.5 iOS app — explicit deferral statement (Category C item 5)

**Status:** DEFERRED to v2 (not in the v1 BUILD_READINESS scope).

**Why iOS waits for v2:**

1. **The iOS app is mostly a viewer, not a driver.** Houston does his real work in the terminal (CLI), the desktop app, and the web. The iOS use case is "check on the lab while away from the laptop" — read activity feed, see standup transcripts, glance at credits, maybe send a quick chat. None of that is critical for the v1 launch.

2. **Native iOS development is expensive.** Tauri 2 has experimental iOS support but it's not production-ready as of 2026-04. The clean iOS path is either Swift (a separate codebase to maintain) or React Native (a separate runtime). Either is a multi-week investment.

3. **The web app on Safari mobile already covers 80% of the use case.** A user can open `hubify-labs.com` on their phone and get a responsive mobile view (already audited per Round A). It's not as nice as a native app but it's not blocking.

4. **Push notifications are the only thing that REQUIRES native iOS.** And we have a fallback for v1: the platform fires push notifications via `ntfy.sh` (or similar) which works as a generic phone push without needing an iOS app.

**What we ship for iOS in v1 (the fallback):**
- The web app at `hubify-labs.com` is mobile-responsive (per Round A audit)
- Push notifications via `ntfy.sh` (web push or the ntfy iOS app — Houston installs that, no Hubify Labs iOS app needed)
- A "Add to Home Screen" PWA manifest so the web app gets a home-screen icon
- Universal links: `hubify://...` URLs open in the web app on iOS (with a graceful fallback to the web URL if Hubify Labs isn't installed)

**v2 plan for native iOS:**
- Re-evaluate Tauri 2 iOS support in Q3 2026
- If still not production-ready, build a Swift/SwiftUI app from scratch — focused on the read-mostly use case (activity feed, standups, credits, chat read + send)
- Share the same `hubify://` URL scheme + deep links + auth tokens with the macOS app
- Submit to Apple App Store (requires Apple Developer Program, which Houston already has)
- Estimated effort: ~3-4 weeks of focused work

**The decision is locked:** v1 ships without a native iOS app. The mobile web + ntfy.sh combination is the v1 mobile story. iOS is v2.

---

## 4. Iteration plan (how this spec gets to 100%)

The macOS spec category has 5 items in the BUILD_READINESS_CHECKLIST. Here's the order:

1. **Write `DESKTOP_APP_SPEC.md`** ← THIS FILE (in progress now)
2. **Tauri shell architecture decision** — Tauri 2 default, this spec confirms
3. **Build `desktop-app-mockup.html`** — the visual layer showing native chrome wrapping the web app
4. **Spec the menu bar app variant** — covered in §2 of this file
5. **iOS app deferral statement** — short paragraph explaining why iOS waits for v2

When all 5 are done, Category C goes from 0% → 100% and the loop moves to the next 0% category.

---

## 5. Open questions

1. **Apple Developer membership** — Houston has it, confirmed?
2. **Bundle identifier** — `com.hubifylabs.app` is the working name. Confirm or override.
3. **App icon design** — needs to be commissioned. Sage green flask icon matching the platform's brand. ~1 day of design work.
4. **Menu bar app — ship in v1 or v2?** Recommend v2 (after the main app is stable). For v1, just ship the main app.
5. **iCloud sync — opt-in or default off?** Recommend default OFF, opt-in via Settings (privacy-first).
6. **Tauri vs Tauri 2** — Tauri 2 is current stable as of 2026-04. Default to 2.x.

---

## 6. What this spec stress-tests

Per the BUILD_READINESS framing, every spec file should explicitly call out what part of the architecture it tests. The macOS spec tests:

- **Tauri 2 as the cross-platform shell strategy** — if it works for macOS, it works for Windows and Linux with minimal changes
- **The `hubify://` URL scheme** as the deep-link layer that all platforms (web, mac, future iOS, future Windows) use the same way
- **The launchd background service pattern** — proves the platform can have always-on agents without requiring a full app window
- **The dock badge + native notification path** — proves the platform can engage Houston without forcing him to look at the app

If this spec ships and the desktop mockup builds successfully, the platform is platform-agnostic for v1.

---

## 7. Where this fits in the bigger picture

This spec is **Category C item 1** of the BUILD_READINESS_CHECKLIST. When all 5 Category C items are done, the loop moves to the next category. The full picture:

| Category | Status | Items |
|---|---|---|
| A. PRD lock | 80% | 51 |
| B. Web mockup | 51% | 49 |
| **C. macOS app** | **20% (this file done = 1/5)** | **5** |
| D. API spec | 0% | 7 |
| E. MCP server | 0% | 7 |
| F. CLI spec | 0% | 8 |
| G. Deployment infra | 0% | 13 |
| H. Migration plan | 67% | 9 |
| I. Houston sign-off | 0% | 7 |

**Category C goes from 0% → 20% with this commit.** The loop demonstrates that it covers all 9 categories, not just mockup polish.
