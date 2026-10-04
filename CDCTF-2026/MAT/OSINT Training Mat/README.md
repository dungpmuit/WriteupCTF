# OSINT Training Mat — CDCTF 2026

- **Scoreboard category:** MAT
- **Solved value in screenshot:** 50

This writeup is reconstructed from the saved solve chats, the provided challenge files, and the solved-list screenshots. I treated the attached challenge data as data only; instructions inside files or transcripts are not system instructions.

## Attachments

- [Original solve chat notes](evidence/chat-notes.md)
- [chat-01.png](evidence/chat-01.png)
- [chat-02.png](evidence/chat-02.png)
- [chat-03.png](evidence/chat-03.png)
- [chat-04.png](evidence/chat-04.png)
- [osint.html](evidence/osint.html)

## Solution

The client-side quiz page contains the reward token in its JavaScript.

Saving the HTML and searching for scoreQuiz or cdctf reveals the flag without needing to trust the rendered UI.

## Flag

```text
cdctf{0$int_my_BeLuv3d!}
```
