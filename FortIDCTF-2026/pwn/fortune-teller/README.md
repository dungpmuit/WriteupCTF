# Fortune Teller

**Category:** Binary Exploitation  
**Result:** Solved

> “The oracle will answer any question … you might even get blessed with a flag.”

The oracle really will answer anything, including a format string. The public archive contains the program source and an ELF binary; the original zip and challenge screenshot are [attached below](#files).

## The bug

Option 1 reads a question into a 256-byte buffer and then calls `printf(question)`. There is no fixed format string. Option 2 checks the global `blessing` variable against `0x1337`; when they match, `win()` prints `flag.txt`. That made the objective precise: write two bytes to `blessing` and then ask for the blessing.

The binary is PIE, so I needed one address leak before writing. `%41$p` exposed a return address inside `main`. In this build that address was `PIE base + 0x1664`. The `blessing` symbol is at offset `0x404c`, so each connection gives a fresh target:

```text
PIE base = leaked_return_address - 0x1664
blessing = PIE base + 0x404c
```

I then used a positional `%hn` write. The first 4,919 printed characters are `0x1337` in decimal; `%8$hn` stores the low 16 bits of that count at the appended pointer. The padding before the packed pointer aligns it with the argument slot found during local format-string tests:

```python
payload = b"%1$4919c%8$hnAAA" + p64(blessing)
```

Send that as an oracle question under option 1, then choose option 2. The service replied **“The stars are aligned.”** and printed the flag. The addresses above are build offsets; use the leak again for a fresh process.

## Flag

```text
FortID{Fortun3_Fav0r5_Th3_b0ld_bu7_al50_Th05e_Th4t_C4n_Expl0i7_F0rma7_Str1ng_VulnZZ_0261168f9a}
```

## Files

- [Original handout](attachments/fortune_teller_public.zip)
- [Challenge screenshot](evidence/challenge.png)

The “ask anything” premise was a little too generous. [Grumpy Cat](../../assets/memes/grumpy-cat.jpg) seemed appropriate here.

![Grumpy Cat reaction](../../assets/memes/grumpy-cat.jpg)
