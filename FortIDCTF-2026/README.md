# FortIDCTF 2026 — Pwn writeups

These notes come from the FortIDCTF challenge pages, the public handouts, and my solve sessions on 10–11 October 2026. The original challenge archives are in each `attachments/` folder. Challenge screenshots are in `evidence/`.

| Challenge | Result | What mattered |
|---|---|---|
| [Fortune Teller](pwn/fortune-teller/README.md) | Solved | Format-string leak and half-word write |
| [GDB SaaS](pwn/gdb-saas/README.md) | Solved | GDB mixed-source disassembly and DWARF |
| [End of Life](pwn/end-of-life/README.md) | Solved | DOS text EOF bypass and 16-bit ROP |
| [Editorial Board](pwn/editorial-board/README.md) | Unsolved; research notes | English-only validator and stack overflow |
| [String Peek and Poke](pwn/string-peek-and-poke/README.md) | Unsolved; research notes | Out-of-bounds `std::string` access |
| [Sticker Booth](pwn/sticker-booth/README.md) | Unsolved; research notes | `mono` overflow and caption alias |

For the unsolved challenges, the writeups stop at the last behavior I could verify. The ideas under **Next step** are hypotheses, not claimed flag paths.

The challenge instances shown in old screenshots are ephemeral. Reproduction on a fresh instance requires replacing their hostnames.
