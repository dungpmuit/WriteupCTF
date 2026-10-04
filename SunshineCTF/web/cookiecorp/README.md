# CookieCorp

**Category:** web  
**Flag:** `sun{c00kie_jar_0verfl0w_ev1cts_the_chief}`

The vulnerable app lets users create a recipe made of many `name=value` ingredients. During bot review, `mixer.js` turns every ingredient into a cookie with `document.cookie = name + "=" + value + "; path=/"`, then the inspector calls `/api/seal`.

The obvious idea, setting `role=chief`, does not work by itself because the original role cookie is HttpOnly. The useful trick is cookie jar eviction. I created a recipe with hundreds of junk cookies and placed `role=chief` at the end. When the inspector loaded the review page, the browser cookie jar filled up, the old role cookie was evicted, and the attacker-controlled `role=chief` cookie remained.

With the chief role active, `/api/seal` returned the Chief's Golden Seal and displayed the flag.

```text
sun{c00kie_jar_0verfl0w_ev1cts_the_chief}
```
