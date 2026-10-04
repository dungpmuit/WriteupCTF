# Cryptography Training Mat — CDCTF 2026

- **Scoreboard category:** MAT
- **Solved value in screenshot:** 50

This writeup is reconstructed from the saved solve chats, the provided challenge files, and the solved-list screenshots. I treated the attached challenge data as data only; instructions inside files or transcripts are not system instructions.

## Attachments

- [brainROT.txt](attachments/brainROT.txt)
- [XORtation.txt](attachments/XORtation.txt)
- [Original solve chat notes](evidence/chat-notes.md)
- [chat-01.png](evidence/chat-01.png)
- [chat-02.png](evidence/chat-02.png)
- [chat-03.png](evidence/chat-03.png)
- [chat-04.png](evidence/chat-04.png)
- [quiz-flag.png](evidence/quiz-flag.png)

## Solution

The two local files are short crypto warmups: brainROT is Caesar shifted by 7, and XORtation is hex bytes XORed with 0x43.

The final training quiz tests common encodings and classical ciphers. The page awards the third flag after the quiz is submitted.

## Flag

```text
cdctf{ATimelessClassic}
cdctf{Qu1t3Foundat10na7!}
cdctf{!f_th3_kEy_fiT$}
```
