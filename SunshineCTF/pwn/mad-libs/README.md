# Mad Libs

**Category:** Pwn  
**Flag:** `sun{f1ll_iN_th3_g0T_eNtry}`

I treated this as a format-string challenge after seeing that the game prints each submitted word with `printf(user_input)`. The binary has PIE, stack canary, and NX enabled, but RELRO is only partial, so the PLT/GOT remains writable.

The exploit first leaked stable stack values. With short payloads, `%43$p` gave a libc return leak and `%47$p` gave a pointer into `main`, which was enough to recover both libc and PIE bases. From there the path was direct: overwrite `printf@GOT` with `system`, then make the next prompt print `/bin/sh` as the format string argument. Once the shell was available, reading the challenge flag returned the token below.

The first failure was not a binary issue: the prompt originally used `chal.sunshinectf.org`, which did not resolve. Switching to the `.games` host made the exploit work.

## Attachments

- [ld-linux-x86-64.so.2](attachments/ld-linux-x86-64.so.2)
- [libc.so.6](attachments/libc.so.6)
- [mad_libs](attachments/mad_libs)

```text
sun{f1ll_iN_th3_g0T_eNtry}
```
