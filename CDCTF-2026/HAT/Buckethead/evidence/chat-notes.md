# Original Chat Notes

These notes are preserved evidence from the solve session. Some attempts may be wrong; the README is the cleaned writeup.

Player

tìm flag ctf

---

Assistant

Flag là:

```text
cdctf{I l1k3 bUCk375}
```

Dữ liệu ẩn trong **2 bit thấp nhất của mỗi kênh R → G → B**, đọc pixel từ trái sang phải, trên xuống dưới. Ghép thành byte, bỏ 3 byte đầu chứa độ dài, thu được flag trên. Giữ nguyên khoảng trắng và chữ hoa/thường.
