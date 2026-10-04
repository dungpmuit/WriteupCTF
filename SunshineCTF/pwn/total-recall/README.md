# Total Recall

**Category:** Pwn  
**Flag:** `sun{r3caLl_ev3Ry_reGist3r_sR0p}`

The program sent an eight-byte stack leak as soon as I connected. That meant I could calculate where the next input would land instead of guessing a stack address. A later read puts data in a stack buffer, and the saved return address is reachable from that input.

The solve script calculates the buffer address as `leak + 8 - 0x88`. I put x86-64 shellcode at the start of the second input; it builds the string `/bin//sh` on the stack and invokes `execve`. After padding up to the saved return address, I overwrote it with the buffer address. When the function returned, execution continued in the shellcode.

I used the resulting shell to read the flag:

## Attachments

- [solve.py](attachments/solve.py)
- [total_recall](attachments/total_recall)

```text
sun{r3caLl_ev3Ry_reGist3r_sR0p}
```

The local script is `D:\ctf\sun\total_recall\solve.py`. Its default host and port may need updating for a live challenge instance.
