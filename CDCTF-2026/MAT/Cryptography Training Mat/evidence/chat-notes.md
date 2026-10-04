# Original Chat Notes

These notes are preserved evidence from the solve session. Some attempts may be wrong; the README is the cleaned writeup.

Player

tìm flag ctf

---

Assistant

Đã tìm đủ **3 flag**:

```text
cdctf{ATimelessClassic}
cdctf{Qu1t3Foundat10na7!}
cdctf{!f_th3_kEy_fiT$}
```

- **BrainROT:** Caesar dịch lùi 7 ký tự.
- **XORtation:** giải hex rồi XOR từng byte với `0x43`.
- **Quiz:** chọn Capitalization, Whitespace, Special Characters → alphabetic substitutions → **Atbash** → Base 16 → XOR → nhập `xor`.

Lưu ý: quiz chấp nhận **Atbash**, dù file BrainROT thực tế dùng Caesar. Nộp từng flag riêng trên CTFd.

![Quiz hoàn thành]
