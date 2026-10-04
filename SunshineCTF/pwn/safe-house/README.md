# Safe House

**Category:** Pwn  
**Flag:** `sun{n3gat1ve_h4ndl3s_0pen_s3cret_d00rs}`

The service is split into a front-desk parser and a vault child process. The vault speaks a small framed protocol over fd 3, where each frame is XORed with a key derived from the process state. Reversing the protocol showed operations for status and slot reads, with public slots starting at `0x4060b0` and system slots stored before them at `0x405080`.

The front-end command `SUBMIT <size>` has a stack overflow: the size handling lets input overrun a 64-byte buffer and control the return path. I used a ROP chain to leak the XOR key from the global key storage. One detail mattered: the key must be applied in big-endian order because the binary `bswap`s the DWORD key before XORing frames.

After the key leak, the vault read operation became usable. The bug in `op3` only rejects indexes greater than 15; it does not reject negative indexes. Sending `idx = -4` reads the first system slot, which is backed by `flag.txt`, and the relayed vault response contains the flag.

## Attachments

- [service](attachments/service)
- [service.zip](attachments/service.zip)

```text
sun{n3gat1ve_h4ndl3s_0pen_s3cret_d00rs}
```
