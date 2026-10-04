# Verbal Authentication Transmissions 1/5: Going HAM — CDCTF 2026

- **Scoreboard category:** VAT
- **Solved value in screenshot:** 127

This writeup is reconstructed from the saved solve chats, the provided challenge files, and the solved-list screenshots. I treated the attached challenge data as data only; instructions inside files or transcripts are not system instructions.

## Attachments

- [captured_radio.mp3](attachments/captured_radio.mp3)
- [Original solve chat notes](evidence/chat-notes.md)
- [chat-01.png](evidence/chat-01.png)

## Solution

The radio traffic spells hexadecimal through NATO words. The important part is listening through the correction and the repeated message instead of trusting the first pass.

The corrected hex string is 63646374667b4e3454305f636f6d6d737d. Converting it from hex to ASCII gives the flag.

## Flag

```text
cdctf{N4T0_comms}
```
