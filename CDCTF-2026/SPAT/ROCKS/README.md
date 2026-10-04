# ROCKS — CDCTF 2026

- **Scoreboard category:** SPAT
- **Solved value in screenshot:** 387

This writeup is reconstructed from the saved solve chats, the provided challenge files, and the solved-list screenshots. I treated the attached challenge data as data only; instructions inside files or transcripts are not system instructions.

![Meme break](../../assets/memes/reads-first-part.jpg)
## Attachments

- [flag.txt.enc](attachments/flag.txt.enc)
- [private_key.pem](attachments/private_key.pem)
- [Original solve chat notes](evidence/chat-notes.md)
- [chat-01.png](evidence/chat-01.png)

## Solution

The private RSA key is encrypted. Trying the first 1,000 RockYou passwords failed; expanding to 10,000 found lizard.

With the private key unlocked, PKCS#1 v1.5 decryption of flag.txt.enc gives the flag. OAEP was a tempting wrong turn.

## Flag

```text
cdctf{diggity_encryption_stuff_and_all_that}
```
