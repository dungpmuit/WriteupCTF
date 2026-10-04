# Original Chat Notes

These notes are preserved evidence from the solve session. Some attempts may be wrong; the README is the cleaned writeup.

Player

tìm flag ctf

---

Assistant

Đã tìm được đủ **3 flag**, nộp từng flag riêng:

1. **Skippy:** `cdctf{SkippingOnMyWay_}`
2. **Static:** `cdctf{AllXOR_Nev3rLupus}`
3. **Quiz:** `cdctf{R2vv1n_!t_UP!}`

Skippy giải bằng bước nhảy `A = 15`. Static giải bằng `cheque XOR key`, kết quả dài 24 ký tự.

[Trang quiz](https://cdctf.net/training/rev_eng_pwn.html) có lỗi chấm câu Static bước 1: so sánh chuỗi `'d'` với mảng `['d']` bằng `===`, nên đáp án đúng vẫn bị chấm sai. Flag thứ ba lấy trực tiếp từ mã JavaScript của trang.
