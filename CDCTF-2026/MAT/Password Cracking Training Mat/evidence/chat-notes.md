# Original Chat Notes

These notes are preserved evidence from the solve session. Some attempts may be wrong; the README is the cleaned writeup.

Player

tìm flag ctf

---

Assistant

Ba flag để nộp riêng từng cái:

```text
cdctf{greatJOB}
cdctf{letmein}
cdctf{R@tc4t_rUL3z!}
```

Đáp án quiz theo thứ tự:

1. **hashcat**
2. **Lựa chọn 3**: `hashcat -a0 -m0 <path to hashes file> <path to rockyou.txt>`
3. `greatJOB`
4. **SHA-256**, `-m1400`
5. `letmein`

Mình đã xác minh hai mật khẩu khớp hash và lấy flag cuối từ mã nguồn [trang bài tập](https://cdctf.net/training/pass_crack.html). Giữ nguyên chữ hoa/thường khi nhập.
