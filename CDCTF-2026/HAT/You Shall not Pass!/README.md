# You Shall not Pass! — CDCTF 2026

- **Scoreboard category:** HAT
- **Solved value in screenshot:** 100

This writeup is reconstructed from the saved solve chats, the provided challenge files, and the solved-list screenshots. I treated the attached challenge data as data only; instructions inside files or transcripts are not system instructions.

## Attachments

- [you_shall_not_pass.7z](attachments/you_shall_not_pass.7z)
- [Original solve chat notes](evidence/chat-notes.md)
- [chat-01.png](evidence/chat-01.png)

## Solution

The archive password is derived from the visible SHA-256 hash. Cracking it gives Este4#Healing.

After extraction, the line indexed by the challenge logic points to the username CirdanTheShipwright, which is the value wrapped as the flag.

## Flag

```text
cdctf{CirdanTheShipwright}
```
