# Editorial Board — research notes

**Category:** Binary Exploitation  
**Result:** Unsolved

> The board wants “clear, polished, human-quality writing” before it will typeset and publish a manuscript.

The public archive contains an ELF binary and `validate.py`. This is a pwn challenge with a gate in front of the memory bug: the manuscript must look like acceptable English prose before it reaches the vulnerable typesetting path.

## What I confirmed

The validator requires 640–900 characters, at least 90 words and four sentences, an allowed punctuation set, and an editorial score from LanguageTool. It also rejects spelling findings and repetitive prose. A clean paragraph passed the structural checks and reached **“Typesetting...”**. The binary's typesetting path then copied an input of at least 640 bytes into a smaller stack region, and the local process crashed. That gave a credible stack overflow, but it did not give a working final payload.

The binary also maps a writable and executable region at a fixed address (`0x656c6000`). The research branch was to jump there with a return address made of validator-safe characters, then decode a second-stage payload. Several decoder designs passed one part of the editorial filter and failed another: spelling, punctuation, or overall score. The saved remote responses contain rejection messages rather than a flag.

## Next step

Keep the accepted prose as the baseline. Change only a few bytes at a time, checking **both** the Python validator and the binary's return path after every change. First demonstrate controlled instruction flow with a harmless marker; then fit a compact decoder and file-read payload within the same validated manuscript. The exact offsets and staging bytes must be confirmed against the provided binary. At the end of these notes, control of a crashing path was observed, but a complete read of `/flag` was not.

The board's scorecard was more demanding than the word count. [Distracted Boyfriend](../../assets/memes/distracted-boyfriend.jpeg) captures how often I switched between punctuation and shellcode bytes.

![Distracted Boyfriend meme](../../assets/memes/distracted-boyfriend.jpeg)

## Files

- [Original handout](attachments/handout.zip)
- [Challenge screenshot](evidence/challenge.png)
