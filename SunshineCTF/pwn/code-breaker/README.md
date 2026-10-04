# Code Breaker

**Category:** Pwn  
**Flag:** `sun{cr4ck_tHe_ciPh3r_fr33_thE_heaP}`

The cache was the first place I looked. Its duplicate-entry behavior lets two entries refer to the same heap object. After freeing the object through one entry, the other still gave me access to the freed memory, so I had a use-after-free.

I used that stale reference to poison the relevant tcache bin. The goal was to make a later allocation reach the callback pointer, then replace the callback with `system@plt`. Once the callback was under my control, I could make the program run a command and print the flag.

The successful run returned:

## Attachments

- [code_breaker](attachments/code_breaker)
- [ld-linux-x86-64.so.2](attachments/ld-linux-x86-64.so.2)
- [libc.so.6](attachments/libc.so.6)

```text
sun{cr4ck_tHe_ciPh3r_fr33_thE_heaP}
```

I saved the exploit as `work/solve_code_breaker.py` in the task directory. The session notes confirm the duplicate-cache bug, tcache poisoning, and callback overwrite, but do not preserve the exact allocation sizes or menu transcript.
