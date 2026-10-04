# Verbal Authentication Transmissions 5/5: You get all that? — CDCTF 2026

- **Scoreboard category:** VAT
- **Solved value in screenshot:** 421

This writeup is reconstructed from the saved solve chats, the provided challenge files, and the solved-list screenshots. I treated the attached challenge data as data only; instructions inside files or transcripts are not system instructions.

## Attachments

- [captured_cred_call.mp3](attachments/captured_cred_call.mp3)
- [cred_call_transcript.txt](attachments/cred_call_transcript.txt)
- [Original solve chat notes](evidence/chat-notes.md)
- [chat-01.png](evidence/chat-01.png)

## Solution

The transcript is Bubble Babble: syllable-like chunks that encode binary while carrying a rolling checksum seed.

Decoding the full hyphenated sequence and round-tripping it with the included solve.py gives the credential flag.

## Flag

```text
cdctf{8u88l3_848813_fl4g_pa55ing}
```
