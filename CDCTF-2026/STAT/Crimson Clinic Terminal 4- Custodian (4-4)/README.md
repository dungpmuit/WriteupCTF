# Crimson Clinic Terminal 4: Custodian (4/4) — CDCTF 2026

- **Scoreboard category:** STAT
- **Solved value in screenshot:** 484

This writeup is reconstructed from the saved solve chats, the provided challenge files, and the solved-list screenshots. I treated the attached challenge data as data only; instructions inside files or transcripts are not system instructions.

## Attachments

- [Original solve chat notes](evidence/chat-notes.md)
- [chat-01.png](evidence/chat-01.png)
- [chat-02.png](evidence/chat-02.png)
- [chat-03.png](evidence/chat-03.png)

## Solution

The final terminal accepts a break-glass request when it is formatted as an audit-worthy medical access event.

The successful request uses reason code BG-01 and chart MRN CC-MRN-41907. The bot grants access and reminds you that the audit trail remains, which is exactly the theme of the flag.

## Flag

```text
cdctf{break_glass_leaves_a_record}
```
