# Print Print Revolution

**Category:** Pwn  
**Flag:** `sun{cust0m_fmtstr_n0_t00ls_4ll0wed}`

This challenge really did make me work without the usual format-string helpers. I started with positional format specifiers and used the output to map values on the stack. That gave me the leaks and argument position I needed to build a write.

The part that took a few tries was keeping the argument offset straight. Appending addresses changes the length of the input, and that can shift where those addresses appear to the format string. An offset that worked for a short probe was not automatically right for the final payload. Once I accounted for that shift, the format string redirected execution into the shell path and I could retrieve the flag.

The working service was `chal.2026.sunshinectf.org:26002`; the hostname tried initially did not resolve. The corrected exploit was saved as `outputs/solve_print_print_revolution.py` in the original task directory.

## Attachments

- [revolution](attachments/revolution)

```text
sun{cust0m_fmtstr_n0_t00ls_4ll0wed}
```
