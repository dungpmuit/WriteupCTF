# Cache Money

**Category:** Pwn  
**Flag:** `sun{s4fe_l1nk1ng_w0nt_s4ve_y0ur_tc4che}`

I began by tracing how the program handles wallet ledgers during transfers and closes. A transfer could leave two wallet slots pointing at the same ledger. Closing one wallet freed the allocation, but the other slot still referenced it, which gave me a use-after-free I could use to inspect and modify a freed tcache chunk.

The heap leak exposed a safe-linked tcache pointer. I used it to recover the value needed to encode a target address. My first poisoning attempt did not work: I had only one chunk in the tcache bin, so glibc popped it and had no second entry from which to return the forged pointer. Adding another freed chunk to that bin fixed the allocation sequence.

I then poisoned an allocation to overlap the wallet table at `0x4040c0`. Writing two forged wallet entries at once turned the table into a pair of convenient read/write objects: one pointed at `puts@GOT`, and the other at `free@GOT`. The `puts` leak gave me the libc base and the address of `system`, so I replaced `free` with `system`.

To finish, I stored `/bin/sh` in a wallet and closed it. The close path called the overwritten `free`, which launched a shell. Reading the flag from there gave me:

## Attachments

- [cache_money](attachments/cache_money)
- [ld-linux-x86-64.so.2](attachments/ld-linux-x86-64.so.2)
- [libc.so.6](attachments/libc.so.6)

```text
sun{s4fe_l1nk1ng_w0nt_s4ve_y0ur_tc4che}
```

The exploit that produced the flag was saved as `work/exploit_cache_money.py` in the original challenge task directory.
