# Blake's Bride — CDCTF 2026

- **Scoreboard category:** SPAT
- **Solved value in screenshot:** 419

This writeup is reconstructed from the saved solve chats, the provided challenge files, and the solved-list screenshots. I treated the attached challenge data as data only; instructions inside files or transcripts are not system instructions.

## Attachments

- [blake.png](attachments/blake.png)
- [Original solve chat notes](evidence/chat-notes.md)
- [chat-01.png](evidence/chat-01.png)
- [chat-02.png](evidence/chat-02.png)

## Solution

The PNG metadata contains three BLAKE2b hashes. The password pattern is wedding-related word plus three digits.

A small wedding-word list plus brute force finds honeymoon069, epithalamium738, and trousseau201. The flag uses them in the metadata order.

## Flag

```text
cdctf{epithalamium738-trousseau201-honeymoon069}
```
