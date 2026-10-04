# bring coines — CDCTF 2026

- **Scoreboard category:** HAT
- **Solved value in screenshot:** 285

This writeup is reconstructed from the saved solve chats, the provided challenge files, and the solved-list screenshots. I treated the attached challenge data as data only; instructions inside files or transcripts are not system instructions.

## Attachments

- [bringcoines.exe](attachments/bringcoines.exe)
- [Original solve chat notes](evidence/chat-notes.md)
- [chat-01.png](evidence/chat-01.png)

## Solution

The executable is a PyInstaller-style Python program. Extracting the code revealed a menu where the coin input accepts a Python expression.

Entering [(H)34] creates the needed coin count, then buying menu option 3, Cowpoke Hat, prints the flag.

## Flag

```text
cdctf{h4t_M0us3_p0k3_FLAG!}
```
