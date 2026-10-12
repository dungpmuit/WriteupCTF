# GDB SaaS

**Category:** Binary Exploitation  
**Result:** Solved

> “Get your `main`'s disassembled for free ...”

The service accepts a base64 ELF and a function name, runs GDB on the uploaded file, and returns the disassembly. The supplied [`server.py`](attachments/server.py) made the trust boundary visible: it copies `flag.txt` beside the uploaded ELF and builds a GDB command with `disassemble {function_name}`. The character blacklist prevents shell metacharacters, but it does not prevent GDB syntax.

## Making GDB show source

GDB's `/s` modifier shows source lines alongside assembly. The function name `/s main` is short and passes the server's filter. It changes the command into `disassemble /s main`.

The other half of the trick is controlling the ELF's debug information. I compiled a tiny function with a line directive naming `flag.txt`:

```c
#line 1 "flag.txt"
int main(){return 0;}
```

```sh
gcc -g -c -o work.o work.c
```

The resulting ELF object has `main` and a DWARF line mapping to `flag.txt`. Upload its base64 bytes, then submit `/s main` at the second prompt. GDB searches for that source filename while producing mixed source and assembly. Because the service put the real `flag.txt` in the same temporary directory, its first line appears in the disassembly output. The remote response showed the file path followed by the flag on line 1.

This took a detour: an expired instance returned HTTP errors at the TLS endpoint, so I used a fresh challenge instance to verify the method. The final flag below came from the GDB response, not from the local source file.

## Flag

```text
FortID{N0_5h3ll_n33d3D_jU57_m41N_4f55dbeeeb}
```

## Files

- [Original server source](attachments/server.py)
- [ELF source used in the solve](evidence/work.c)
- [Compiled ELF object used in the solve](evidence/work.o)
- [Challenge screenshot](evidence/challenge.png)

My face when a disassembler starts reading its neighbor's files: [Grumpy Cat](../../assets/memes/grumpy-cat.jpg).

![Grumpy Cat reaction](../../assets/memes/grumpy-cat.jpg)
