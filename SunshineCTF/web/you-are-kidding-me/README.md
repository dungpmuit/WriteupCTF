# You Are Kidding Me

**Category:** Web  
**Flag:** `sun{h0tw1r3d_4dm1n_jwt}`

I focused on the JWT verification logic. The server used the token's `kid` header to choose a key, and that value was treated like a file path. Since the stylesheet was public, I could read its contents and use those same bytes as the HMAC secret.

I made an HS256 token claiming the `editor` role and set `kid` to `/app/static/style.css`. I signed it with the contents of `/static/style.css`, sent it in the `token` cookie, and visited `/admin`. The server loaded the stylesheet as its verification key, accepted the signature, and let me into the protected page where the flag was shown.

```text
sun{h0tw1r3d_4dm1n_jwt}
```

The bug is the trust placed in `kid`: key identifiers should map to a fixed set of configured keys, rather than being used directly to read an arbitrary path.
