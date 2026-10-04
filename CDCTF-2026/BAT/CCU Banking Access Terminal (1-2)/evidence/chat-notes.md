# Original Chat Notes

These notes are preserved evidence from the solve session. Some attempts may be wrong; the README is the cleaned writeup.

Player

tìm flag ctf

---

Player

tìm flag ctf

---

Assistant

Flag là:

```text
cdctf{b7a89b15f1dccc5c_vault_seal_released_79e01577}
```

Mình khai thác overflow ở phần transfer memo: buffer 64 byte nhưng chương trình `read` tới `0x100`, rồi ROP vào `vault_maintenance(0xc0ffee)` bằng gadget `pop rdi; ret` tại `0x4018d1`.
