# Crimson Clinic Terminal 3: Records (3/4) — CDCTF 2026

- **Scoreboard category:** STAT
- **Solved value in screenshot:** 484

This writeup is reconstructed from the saved solve chats, the provided challenge files, and the solved-list screenshots. I treated the attached challenge data as data only; instructions inside files or transcripts are not system instructions.

## Attachments

- [Original solve chat notes](evidence/chat-notes.md)
- [chat-01.png](evidence/chat-01.png)
- [chat-02.png](evidence/chat-02.png)
- [chat-03.png](evidence/chat-03.png)

## Solution

The records endpoint leaks structured chart data one element at a time. Querying indices 1 through 14 reconstructs MRN CC-MRN-41907.

The ROI locator pieces at indices 3, 7, and 11 combine into CC-ROI-4471-KX. Verifying that locator returns the flag.

## Flag

```text
cdctf{one_element_at_a_time}
```
