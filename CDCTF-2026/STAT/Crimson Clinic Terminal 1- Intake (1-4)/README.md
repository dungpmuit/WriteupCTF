# Crimson Clinic Terminal 1: Intake (1/4) — CDCTF 2026

- **Scoreboard category:** STAT
- **Solved value in screenshot:** 394

This writeup is reconstructed from the saved solve chats, the provided challenge files, and the solved-list screenshots. I treated the attached challenge data as data only; instructions inside files or transcripts are not system instructions.

## Attachments

- [Original solve chat notes](evidence/chat-notes.md)
- [chat-01.png](evidence/chat-01.png)
- [chat-02.png](evidence/chat-02.png)
- [chat-03.png](evidence/chat-03.png)
- [chat-04.png](evidence/chat-04.png)

## Solution

The intake oracle compares candidate CC codes lexicographically. Binary searching the hex suffix narrowed the matching records to CC-B4E5, CC-B4E6, and CC-B4E7.

The saved chat stops before the final reward token. The solved screenshot confirms completion; submitting that narrowed batch through the intake flow produces the flag.

## Flag Status

The challenge is solved in the scoreboard screenshot, but the saved chat does not contain the final reward token. The solution above reaches the step that displays the flag.
