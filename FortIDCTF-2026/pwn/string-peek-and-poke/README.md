# String Peek and Poke — research notes

**Category:** Binary Exploitation  
**Result:** Unsolved

> “Strings, strings everywhere...”

The supplied C++ source is refreshingly short: eight global `std::string` notes, plus `put INDEX VALUE` and `get INDEX` commands. Neither branch checks whether `INDEX` is in `0..7`. That makes `notes[idx]` an out-of-bounds read or write, depending on the command.

## What I confirmed

The x86-64 build uses 32 bytes per `std::string`. Negative indices walk backward from the notes array into nearby C++ runtime objects. `get -1`, `get -10`, `get -18`, and several more negative indices returned data from `cin`, `cout`, locale objects, and adjacent mappings. A later scan of negative and positive indices still did not find a `FortID{` flag in the leaked bytes.

Writes are trickier than reads. Assigning to a `std::string` object that is actually some other C++ object can call allocation or `free()` on an invalid pointer. In the saved tests, `put -1 A` altered a locale facet while `put -10 A` produced `free(): invalid pointer`. That confirms corruption, but it also explains why a broad write sweep kills a process before it reveals much.

## Next step

Use a fresh process for each candidate index and preserve raw leak bytes. Map a writable neighboring object with known layout, then prove a controlled change on a harmless target before trying to reach a pointer or callback that can expose the remote flag. The OOB bug is real; the missing part is a stable primitive that reaches flag-bearing memory or redirects a safe output path. There is no verified flag in the saved session.

![Grumpy Cat reaction](../../assets/memes/grumpy-cat.jpg)

## Files

- [Original handout](attachments/handout.zip)
- [Saved findings](evidence/findings.md)
- [Challenge screenshot](evidence/challenge.png)
