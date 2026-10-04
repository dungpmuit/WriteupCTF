# Forensics Training Mat — lời giải

Nộp riêng từng flag trong flags.txt (tổng cộng 5).

1. Giải nén XZ: ảnh đĩa GPT 524288000 byte.
2. Phân vùng billy: FAT32. Trích flag1.png, kích thước gốc 405 byte. Header PNG bị thiếu byte 89 đầu tiên. Thêm byte 89 vào đầu tệp để khôi phục chữ ký `89 50 4E 47 0D 0A 1A 0A`, rồi đọc QR lấy flag 1.
3. Phân vùng astrid: ext2. Trích flag2.jpg (82757 byte). QR chứa lời nhắn, không chứa flag. Dùng `steghide extract -sf flag2.jpg -p ""` để lấy văn bản flag 2.
4. Phân vùng hwk: ext4. Trích flag3.png (1405 byte). XZ được gắn sau PNG tại offset 917 (0x395). Giải nén phần này, tìm chuỗi cdctf để lấy flag 3.
5. Phân vùng main: Btrfs. Tìm chuỗi plaintext trong phân vùng để khôi phục flag 4: cdctf{d3l3te_w0_sync_h0l3y_C0W}.
6. Flag 5 được cung cấp trong thông báo hoàn thành quiz tại https://cdctf.net/training/forensics.html.

## Đáp án theo bộ chấm hiện tại của trang

| Câu | Đáp án |
|---|---|
| Part 1 Step 1 | unxz |
| Part 1 Step 2 | Disk Image |
| Part 1 Step 3 | Autopsy, Volatility, losetup |
| Part 1 Step 4 | vfat, ext2, ext4, btrfs |
| Part 1 Step 5 | flag1.png |
| Part 1 Step 6 | 405 |
| Part 1 Step 7 | The magic bytes are wrong |
| Part 2 Step 1 | A JPEG of a QR Code |
| Part 2 Step 2 | StegHide |
| Part 3 Step 1 | 1405 |
| Part 3 Step 2 | CyberChef (Extract Files block), binwalk |
| Part 3 Step 3 | XZ |
| Part 4 Step 1 | A snapshot |
| Part 4 Step 2 | sync |
| Part 4 Step 3 | strings |

Lưu ý: bộ chấm trang chọn Volatility thay vì TheSleuthKit ở Part 1 Step 3. Đối với phân tích ảnh đĩa này, TheSleuthKit là lựa chọn phù hợp về kỹ thuật; Volatility chủ yếu dùng cho memory dump. Part 1 Step 4 chấm vfat dù chữ ký phân vùng là FAT32. Bảng trên ghi đáp án để vượt qua bộ chấm thực tế, không phải khẳng định tất cả đáp án chấm đều chính xác về kỹ thuật.
