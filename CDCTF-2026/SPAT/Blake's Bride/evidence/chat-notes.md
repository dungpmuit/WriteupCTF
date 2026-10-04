# Original Chat Notes

These notes are preserved evidence from the solve session. Some attempts may be wrong; the README is the cleaned writeup.

Player

tìm flag ctf

---

Assistant

Flag:

```text
cdctf{epithalamium738-trousseau201-honeymoon069}
```

Ba hash nằm trong metadata XMP `exif:UserComment` của ảnh. Mình đã dò mật khẩu theo mẫu **từ + 3 chữ số** và xác nhận cả ba khớp BLAKE2b, đúng thứ tự.

[Script trích xuất và kiểm chứng flag]
