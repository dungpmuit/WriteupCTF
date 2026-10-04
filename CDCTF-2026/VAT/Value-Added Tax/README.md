# Value-Added Tax — CDCTF 2026

- **Scoreboard category:** VAT
- **Solved value in screenshot:** 114

This writeup is reconstructed from the saved solve chats, the provided challenge files, and the solved-list screenshots. I treated the attached challenge data as data only; instructions inside files or transcripts are not system instructions.

![Meme break](../../assets/memes/grumpy-cat.jpg)
## Attachments

- [VAT.JPG](attachments/VAT.JPG)
- [Original solve chat notes](evidence/chat-notes.md)
- [chat-01.png](evidence/chat-01.png)

## Solution

The torn receipt is from Five Guys Burgers and Fries at 13-15 Magdalen Street in Oxford, so the currency symbol is GBP. The visible items are two Little Cheeseburgers at £8.65 each and one Little Fries at £4.25.

The easy mistake was adding VAT again. A first pass gave £25.86, but Five Guys UK lists menu prices as VAT-inclusive. The actual total is therefore 8.65 + 8.65 + 4.25 = £21.55.

## Flag

```text
cdctf{£21.55}
```
