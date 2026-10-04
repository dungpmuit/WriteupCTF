# Crimson Clinic Terminal 1: Intake (1/4) — CDCTF 2026

- **Scoreboard category:** STAT
- **Solved value in screenshot:** 394

## Attachments

- [Original solve chat notes](evidence/chat-notes.md)
- [chat-01.png](evidence/chat-01.png)
- [chat-02.png](evidence/chat-02.png)
- [chat-03.png](evidence/chat-03.png)
- [chat-04.png](evidence/chat-04.png)

## Solution

The intake oracle compares candidate CC codes lexicographically. Binary searching the hex suffix narrowed the matching records to CC-B4E5, CC-B4E6, and CC-B4E7.

The remaining step is to submit that narrowed batch through the intake flow. That completes the challenge and displays the flag.

## Result

After the final step, the challenge displays the flag. I did not keep the exact flag text in my notes.
