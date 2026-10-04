# Planetary Probe

**Category:** Web  
**Flag:** `sun{bl1nd_psqli_2_rc3_P4Nd0FyZt8k2}`

The `planet` parameter on `/probe` was being used in a PostgreSQL query. The page did not display the query result, so I needed a way to ask the database yes-or-no questions. I tested whether an injected condition could change how long the request took.

It could. The injection accepted stacked queries, and PostgreSQL's `COPY ... TO PROGRAM` let me run a command on the challenge server. I made the command sleep only when a condition about the flag was true. A delayed response meant yes; a normal response meant no. That gave me a timing oracle for reading data without seeing it in the response body.

Timing measurements were noisy, so I read the file a byte at a time and used binary search to narrow down each byte's value. I repeated checks when timings disagreed, then continued until I had read the closing brace. That last pass also caught a case-sensitive detail: the `P` in the flag is uppercase.

```text
sun{bl1nd_psqli_2_rc3_P4Nd0FyZt8k2}
```
