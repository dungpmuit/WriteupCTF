# Used Goods of Tomorrow

**Category:** Web  
**Flag:** `sun{1_l0v3_fr33_stuff}`

I went straight to the GraphQL endpoint and asked it for its schema. Introspection showed fields and mutations that the storefront did not expose. One of them, the vendor synchronization path, returned a vendor key. That key led to a list of promotion codes, including `FOUNDERS-100`.

With an account token in hand, I used the `placeOrder` mutation on listing `4042` and supplied that promo code. The order cost no credits, and the API response included the flag:

```text
sun{1_l0v3_fr33_stuff}
```

The solve came together by following the extra GraphQL fields: introspect the schema, retrieve the vendor key, find the promo code, and apply it to the right listing.
