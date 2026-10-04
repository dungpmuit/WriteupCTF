# Verbal Authentication Transmissions 4/5: What the helly — CDCTF 2026

- **Scoreboard category:** VAT
- **Solved value in screenshot:** 484

This writeup is reconstructed from the saved solve chats, the provided challenge files, and the solved-list screenshots. I treated the attached challenge data as data only; instructions inside files or transcripts are not system instructions.

## Attachments

- [OTP_CODES_VAT.mp3](attachments/OTP_CODES_VAT.mp3)
- [Original solve chat notes](evidence/chat-notes.md)
- [chat-01.png](evidence/chat-01.png)
- [transcript.txt](evidence/transcript.txt)

## Solution

The six-word groups are S/KEY-style one-time password words. Each word contributes 11 bits, giving 64 bits of data plus checksum bits.

The matching derivation was MD5 folded by XORing the two digest halves. Cracking the folded target against RockYou yielded idontcare1, and the saved scripts verify the OTP chain.

## Flag

```text
cdctf{idontcare1}
```
