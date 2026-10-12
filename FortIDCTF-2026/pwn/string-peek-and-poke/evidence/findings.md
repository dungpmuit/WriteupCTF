# String Peek and Poke — findings

- Type: Pwn / binary exploitation.
- `notes[idx]` has no bounds check; each index moves by 32 bytes because `std::string` is 32 bytes on x86-64.
- `notes` is at PIE-relative `0x203260`; `cout` is at `0x203020`, `cin` at `0x203140`.
- Safe reads showed no `FortID{` in the adjacent `cout`, `cin`, locale, libstdc++, or GOT-related leaks.
- `put -1 A` writes into the cached ctype/facet object and can survive one command; `put -10 A` reaches a different facet and reliably aborts with `free(): invalid pointer`.
- `put -27 A` also aborts; it reaches the reserved/GOT area.
- The endpoint `string-peek-and-poke-69ade9f10d45.inst17.ctf.fortid.com` is currently not returning a usable second prompt after the last crash, so a fresh instance is required for further exploit testing.
