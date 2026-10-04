# Market History — CDCTF 2026

- **Scoreboard category:** SAT
- **Solved value in screenshot:** 460

This writeup is reconstructed from the saved solve chats, the provided challenge files, and the solved-list screenshots. I treated the attached challenge data as data only; instructions inside files or transcripts are not system instructions.

## Attachments

- [Original solve chat notes](evidence/chat-notes.md)
- [chat-01.png](evidence/chat-01.png)

## Solution

The target is an EVE Online market-history lookup. The relevant station is Traders'R'Us in Orvolle, station ID 1033196707294.

On Adam4EVE, filtering station income since 2026-05-16 shows the maximum relevant FromBuyorder value on 2026-08-29: 11,680,000 ISK.

## Flag

```text
cdctf{2026-08-29_11680000}
```
