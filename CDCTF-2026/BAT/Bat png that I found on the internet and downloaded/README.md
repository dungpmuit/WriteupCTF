# Bat png that I found on the internet and downloaded — CDCTF 2026

- **Scoreboard category:** BAT
- **Solved value in screenshot:** 234

This writeup is reconstructed from the saved solve chats, the provided challenge files, and the solved-list screenshots. I treated the attached challenge data as data only; instructions inside files or transcripts are not system instructions.

## Attachments

- [BatPic.png](attachments/BatPic.png)
- [Original solve chat notes](evidence/chat-notes.md)
- [chat-01.png](evidence/chat-01.png)
- [chat-02.png](evidence/chat-02.png)
- [flag-green-lsb.png](evidence/flag-green-lsb.png)

## Solution

The image hides a message in the green-channel least significant bit. Visualizing (G & 1) as black/white reveals the text directly.

The decoded visualization is included in evidence for quick checking.

## Flag

```text
cdctf{I_lik3_ba7S}
```
