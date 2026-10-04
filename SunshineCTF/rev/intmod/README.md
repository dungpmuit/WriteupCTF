# IntMod

**Category:** RE  
**Flag:** `sun{I_L0v3_Int3rrupts&SelfMod!!!}`

This reverse challenge is an ELF64 flag checker built around a small VM and self-modifying/signal-driven execution. The binary reads exactly 33 bytes, which matches `sun{` plus 28 content characters plus `}`. Fake inputs reach `Nope`, while the VM uses `int3`, `ud2`, and divide faults as part of the execution machinery.

I built a Unicorn emulator that could run the binary on Windows and emulate the registered `SIGTRAP`, `SIGILL`, and `SIGFPE` handlers. Once the handler path worked, fake flags produced the real `Nope` result, giving a trustworthy oracle. Dumping the decoded VM stream showed opcodes for add, xor, multiply, rotate, swap, `intmod`, compare, and nop.

The key observation was that from program counter 103 onward, the VM stops mutating the five qword state values and only performs `intmod` plus compare operations. Those checks form 40 linear equations modulo 65521 over the 40-byte state. Solving that linear system and then reversing the earlier VM operations recovered the original flag plus `0x07` padding. Running the recovered input through the emulator printed `Correct`.

## Attachments

- [intmod](attachments/intmod)

```text
sun{I_L0v3_Int3rrupts&SelfMod!!!}
```
