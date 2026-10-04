# Password Cracking Training Mat — CDCTF 2026

- **Scoreboard category:** MAT
- **Solved value in screenshot:** 50

This writeup is reconstructed from the saved solve chats, the provided challenge files, and the solved-list screenshots. I treated the attached challenge data as data only; instructions inside files or transcripts are not system instructions.

## Attachments

- [hashes.txt](attachments/hashes.txt)
- [Original solve chat notes](evidence/chat-notes.md)
- [chat-01.png](evidence/chat-01.png)
- [chat-02.png](evidence/chat-02.png)
- [chat-03.png](evidence/chat-03.png)
- [chat-04.png](evidence/chat-04.png)
- [pass_crack.html](evidence/pass_crack.html)

## Solution

The hashes file contains an MD5 target and a SHA-256 target. Hashcat mode 0 cracks greatJOB, and mode 1400 cracks letmein.

The quiz then reinforces hashcat, hash modes, and recovered words. The success branch returns the Ratcat-themed flag.

## Flag

```text
cdctf{greatJOB}
cdctf{letmein}
cdctf{R@tc4t_rUL3z!}
```
