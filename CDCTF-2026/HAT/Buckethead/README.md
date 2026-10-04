# Buckethead — CDCTF 2026

- **Scoreboard category:** HAT
- **Solved value in screenshot:** 100

This writeup is reconstructed from the saved solve chats, the provided challenge files, and the solved-list screenshots. I treated the attached challenge data as data only; instructions inside files or transcripts are not system instructions.

![Meme break](../../assets/memes/distracted-boyfriend.jpeg)
## Attachments

- [buckethead_zombie.png](attachments/buckethead_zombie.png)
- [Original solve chat notes](evidence/chat-notes.md)
- [chat-01.png](evidence/chat-01.png)
- [chat-02.png](evidence/chat-02.png)

## Solution

The PNG hides data in the two lowest bits of each RGB channel, read row-major. One-bit LSB was too shallow; two-bit extraction revealed a little-endian length header.

The first three bytes encode length 22, and the following payload decodes to the flag.

## Flag

```text
cdctf{I l1k3 bUCk375}
```
