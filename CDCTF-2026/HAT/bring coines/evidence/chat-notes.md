# Original Chat Notes

These notes are preserved evidence from the solve session. Some attempts may be wrong; the README is the cleaned writeup.

Player

tìm flag ctf

---

Assistant

Flag là:

```text
cdctf{h4t_M0us3_p0k3_FLAG!}
```

File được đóng gói bằng PyInstaller. Trong hàm `hat_menu`, flag được lưu dưới dạng các mã ASCII.

Để hiện flag trong chương trình: nhập `[(H)34]` ở câu hỏi số coins, sau đó chọn `3` (Cowpoke Hat).
