# Reverse Engineering & Pwn Training Mat — CDCTF 2026

- **Scoreboard category:** MAT
- **Solved value in screenshot:** 143

This writeup is reconstructed from the saved solve chats, the provided challenge files, and the solved-list screenshots. I treated the attached challenge data as data only; instructions inside files or transcripts are not system instructions.

## Attachments

- [skippy.py](attachments/skippy.py)
- [static](attachments/static)
- [Original solve chat notes](evidence/chat-notes.md)
- [chat-01.png](evidence/chat-01.png)
- [chat-02.png](evidence/chat-02.png)
- [chat-03.png](evidence/chat-03.png)
- [chat-04.png](evidence/chat-04.png)

## Solution

skippy.py permutes characters by stepping through the alphabet/string with a modular stride. Inverting that permutation recovers the first flag.

The static binary's cheque data XORs with a 24-byte key to recover the second flag. The quiz page has a strict JavaScript comparison bug, so the flag was recovered from the source.

## Flag

```text
cdctf{SkippingOnMyWay_}
cdctf{AllXOR_Nev3rLupus}
cdctf{R2vv1n_!t_UP!}
```
