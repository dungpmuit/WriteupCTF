# Original Chat Notes

These notes are preserved evidence from the solve session. Some attempts may be wrong; the README is the cleaned writeup.

Player

tìm flag ctf

---

Assistant

Flag là:

```text
cdctf{N4T0_comms}
```

Đoạn radio đọc chuỗi hex, dùng NATO để biểu diễn chữ: **Bravo → B, Echo → E, Foxtrot → F, Delta → D**.

Sau lời “Correction” và lần đọc lại, chuỗi thu được:

```text
63646374667b4e3454305f636f6d6d737d
```

Chuyển hex sang ASCII cho ra flag trên.
