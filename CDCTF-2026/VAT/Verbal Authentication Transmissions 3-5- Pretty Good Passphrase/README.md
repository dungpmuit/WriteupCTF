# Verbal Authentication Transmissions 3/5: Pretty Good Passphrase — CDCTF 2026

- **Scoreboard category:** VAT
- **Solved value in screenshot:** 456

This writeup is reconstructed from the saved solve chats, the provided challenge files, and the solved-list screenshots. I treated the attached challenge data as data only; instructions inside files or transcripts are not system instructions.

## Attachments

- [VAT_key](attachments/VAT_key)
- [voicemail.mp3](attachments/voicemail.mp3)
- [Original solve chat notes](evidence/chat-notes.md)
- [chat-01.png](evidence/chat-01.png)
- [recovered.asc](evidence/recovered.asc)

## Solution

The voicemail words are from the PGP word list. Each word maps to a byte, and the odd/even word column matters. After reconstructing the bytes, the result is an OpenPGP message.

Import VAT_key and decrypt the recovered armored message with passphrase Password123!. The recovered .asc file is included under evidence so the transcription work is reproducible.

## Flag

```text
cdctf{pr3t7y_g00d_piv4cy_fl4G}
```
