# You.md project log convention

Agents append to `log.md` after meaningful changes.
Other agents read it at session start to see recent work.
The log travels with the project's git repo.

## Format

```
## <UTC ISO timestamp> — <agent name>
<message>
```

## Usage

  youmd project log "what I changed"   # append entry
  youmd project log                     # read last 15 entries

## Agent name

Set `YOUMD_AGENT_NAME` env to identify the writing agent.
Default: "agent"
