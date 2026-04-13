

## 2026-04-13 — Compute optimization + sidebar collapse bug

### Houston substantive messages, verbatim

**~afternoon PT — Compute self-optimization for PRD**
> Okay, one thing that we need to add is some self-optimizations on scripts and things when we're running large data on RunPod. There have been many times where a few things have happened that I just want to make sure we account for in the PRD. That would be like: - Hey, is there a way we can run this faster? How can we chunk things differently, process things differently, to speed it up, and then run a few little test runs before you run any job, like a long-running big data set? - Those learnings, I'm just figuring out how to optimize before you run it, can be almost as valuable as what you find when you run it. The other thing would be just balancing time, speed, and cost when deciding what pod or CPU or GPU to run on RunPod. If I choose a cheaper pod but it runs for longer, that may actually end up costing more than if I pick the faster pod that finishes faster, even if it's more expensive. I just want to add some notes on this stuff to the PRD. I'm going to look through our actual big bounce project for any speed and selection and any sort of things related to whatever I'm talking about here, to add to the PRD with real examples and actually get it going.

**~afternoon PT — Lab Site vibe coding layout is terrible, fix it**
> the vibe coding style layout for the Lab Site is TERRIBLE ... that right side panel should not exist but it can just be another view for details on top of the right side tab view - which should have highest quality views for Code where you should basically just reuse our existing files in the right side there just like most vibe coding platforms typically have like Code (files), Preview (live sandbox render/testing), Settings (for env vars, subdomain, etc etc), a deploy button on the top, etc... and the main left side menu should be collapsed by default when the lab site view is open too please

**~afternoon PT — Sidebar collapse CSS bug report**
> Okay, one other thing I notice also is that the main side menu, when it's collapsed, is like the icons and everything properly collapse, but it stays the same size. It's just like a wide single column side panel, so it looks really weird to fix that.

---

## 2026-04-12 — Lab Site vision · vibe-coded research sites as first-class feature

### Houston substantive messages, verbatim

**~afternoon PT — Lab Site feature gap identified, full vision dump**
> ok another thing i want to dial in actually now is the Lab Site - I don't konw when but that got lost at some point and basically should just be a custom right side pane vercel sandbox to vide code via the main existing orchestrator or terminal chat - and the custom Lab sites should follow a standard organization structure that matches style and structure of the hubify labs design by default but the user/lab owner can basically vibe code to change the style, and anything about their site for their lab, .. this is one of the things that was kinda the original problem you know looking at how i was updating the bigbounce Site and Papers and basically using the site to keep track of the research etc the app itself solves a lot of the problems that i was trying to solve with the site but a new clean version of what should actually be publishable as part of the research sites should be standardized and we should figure that part out add it to the PRD properly updated and ensure we still hvae the ability to preview the site and subdomain and just chat with our orcehstrator to customize and build out the site and obviously we should already have some scoped out sub agents etc for maintaining and updating the lab sites etc too ya know i don't see that in th ecurrent mockup/uis

**~afternoon PT — EXECUTE confirmation + pivot the loop to this work**
> yes EXECUTE THIS and do not forget this message or this plan this is what the loop should focus on now and ensuring our PRD and full plan to go from mockup to fully migrating existing bigbounce to the new lab setup and launch the new labs etc all reayd to rock
> ok another thing i want to dial in actually now is the Lab Site - I don't konw when but that got lost at some point and basically should just be a custom right side pane vercel sandbox to vide code via the main existing orchestrator or terminal chat - and the custom Lab sites should follow a standard organization structure that matches style and structure of the hubify labs design by default but the user/lab owner can basically vibe code to change the style, and anything about their site for their lab, .. this is one of the things that was kinda the original problem you know looking at how i was updating the bigbounce Site and Papers and basically using the site to keep track of the research etc the app itself solves a lot of the problems that i was trying to solve with the site but a new clean version of what should actually be publishable as part of the research sites should be standardized and we should figure that part out add it to the PRD properly updated and ensure we still hvae the ability to preview the site and subdomain and just chat with our orcehstrator to customize and build out the site and obviously we should already have some scoped out sub agents etc for maintaining and updating the lab sites etc too ya know i don't see that in th ecurrent mockup/uis

---

## 2026-04-11 — v4 frustration · demands actual AgenticUI layout work NOW

**~00:15 PT — Houston furious at lack of visible progress**
> hows it going? its all mostly looking the same still what is going on ? how about actually getting this shit done? utilizing some of the actual fonts and layouts from the agenticui figma in our app? just thoughts im fucking tired of waiting this should not be taking so long bro wtf... you cloned one of the agent management full pages into code from figma in like 5 minutes and now 45mins later and i don't even see anything what is going on ?

**Key context:** Houston references that a previous session cloned the agent-management page (233:1397) from Figma into working HTML in ~5 minutes. He expects the same speed for pulling other layouts. 45 minutes of context recovery, file restoration, and metadata exploration produced zero visible changes to v4.

## 2026-04-11 — AgenticUI v4 Polish Sprint

### Houston substantive messages, verbatim

**19:55 PT — Approved AgenticUI→v4 plan, defined execution protocol**
> yes please save this plan in a /project-context/ directory file and update claude.md to know this is what we are working on now - not using Figma mcp now except for just screenshot of an associated component potentially as needed to cross-check styles of our new internal agenticui directory code base to improve and polish etc etc ... but i want you workin gon this FOR /v4/ expliclitly and in these phases planned and looped via a specific cron for this until it is done and by done i must approve it and confirm it is done
>
> [included full 4-pass plan: Token foundation → Component swap → Spacing/density → Typography polish]
> The 20K-line index.html is where 80% of the impact lives. The other 4 files are smaller and will mostly inherit the token changes.
