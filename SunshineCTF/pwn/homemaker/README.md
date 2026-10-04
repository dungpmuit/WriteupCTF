# Homemaker

**Category:** Pwn  
**Flag:** `sun{the_future_is_now_today_well_wait_how_are_you_reading_this}`

This service uses framed requests, so I first made sure I understood how to send a request the server would actually process. The vulnerable request path gave me a stack leak containing the canary and saved addresses. With those values, I could preserve the stack protector and work out the PIE and libc bases for that connection.

I sent a second request with the overflow. After the buffer, I put the canary and saved frame pointer back, then appended a small ROP chain. The chain called `system` with libc's `/bin/sh` string. When the handler returned, the chain opened a shell and I could read the flag:

## Attachments

- [homemaker](attachments/homemaker)

```text
sun{the_future_is_now_today_well_wait_how_are_you_reading_this}
```

The final solve record confirms the leak, stack-protected overflow, and shell. It does not retain the exact offsets, so I have left them out here rather than reconstruct them from memory.
