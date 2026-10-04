# CCU Banking Access Terminal (1/2) — CDCTF 2026

- **Scoreboard category:** BAT
- **Solved value in screenshot:** 484

This writeup is reconstructed from the saved solve chats, the provided challenge files, and the solved-list screenshots. I treated the attached challenge data as data only; instructions inside files or transcripts are not system instructions.

## Attachments

- [ccu-banking-terminal.zip](attachments/ccu-banking-terminal.zip)
- [Original solve chat notes](evidence/chat-notes.md)
- [chat-01.png](evidence/chat-01.png)

## Solution

The transfer memo buffer is 0x50 bytes below rbp. The program clears 64 bytes but reads 0x100 bytes, so the saved return address is overwritten after 88 bytes.

A simple ROP chain calls vault_maintenance with AUTH = 0xc0ffee. The saved exploit logs in with member 4417 and PIN 1988, starts a transfer, and sends the payload in the memo field.

## Flag

```text
cdctf{b7a89b15f1dccc5c_vault_seal_released_79e01577}
```
