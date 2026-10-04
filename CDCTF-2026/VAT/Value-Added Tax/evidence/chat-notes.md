# Original Chat Notes

These notes are preserved evidence from the solve session. Some attempts may be wrong; the README is the cleaned writeup.

Player

tìm flag ctf

---

Assistant

Flag nên thử: **`cdctf{£25.86}`**

Hóa đơn có hai burger giá £8.65 và khoai tây £4.25:

- Tổng: `8.65 + 8.65 + 4.25 = £21.55`
- VAT tại Anh: [20%](https://www.gov.uk/vat-rates) → `£4.31`
- Tổng cộng VAT: **£25.86**

Kết quả này giả định các giá trên hóa đơn chưa gồm VAT, theo cách diễn đạt của đề. Chưa xác nhận bằng hệ thống chấm.

---

Player

sai flag r

---

Assistant

Thử **`cdctf{£21.55}`**.

Mình đã cộng VAT hai lần ở đáp án trước. [Điều khoản Five Guys, mục 2.3](https://www.fiveguys.co.uk/legal/) xác nhận giá niêm yết **đã gồm VAT**.

Vậy tổng thanh toán là `£8.65 + £8.65 + £4.25 = £21.55`. Chưa xác nhận qua hệ thống chấm.

---

Player

Hãy viết write-up cho tôi, hãy viết giống con người và có thể chèn meme nếu cần

---

Assistant

# Value-Added Tax — cdCTF Write-up

**Category:** OSINT  
**Flag:** `cdctf{£21.55}`

## Đề bài

Đề cho một bức ảnh hóa đơn bị rách và yêu cầu tìm tổng số tiền người mua đã trả, bao gồm VAT. Flag có dạng:

```text
cdctf{[CurrencySymbol]XX.XX}
```

Phần tổng tiền đã biến mất, nhưng tên cửa hàng, địa chỉ và giá từng món vẫn còn đọc được. Nhìn qua thì tưởng chỉ cần cộng tiền rồi thêm thuế. Và mình đã mắc đúng cái bẫy đó.

## Đọc hóa đơn

Các thông tin còn thấy được:

```text
FIVE GUYS BURGERS AND FRIES
13–15 Magdalen Street
14/07/2024

LITTLE CHEESEBURGER       8.65
  ALL THE WAY
LITTLE CHEESEBURGER       8.65
  ALL THE WAY
LITTLE FRIES             4.25
```

Hai dòng **ALL THE WAY** là lựa chọn topping cho burger, không phải hai món tính tiền riêng.

Địa chỉ và tên cửa hàng cho thấy đây là Five Guys tại Anh, nên đơn vị tiền tệ cần dùng là bảng Anh: **£**.

Cộng ba món:

```text
8.65 + 8.65 + 4.25 = £21.55
```

## Cái bẫy VAT

Vì đề nhấn mạnh “plus VAT”, hướng đầu tiên mình thử là cộng thêm 20%:

```text
£21.55 × 1.20 = £25.86
```

Flag `cdctf{£25.86}` bị hệ thống từ chối.

> Mình: Thấy VAT thì cộng thêm 20%, quá đơn giản.  
> Hệ thống chấm: **Incorrect.**  
> Mình: Có vẻ đơn giản hơi sớm.

Vấn đề nằm ở giả định rằng giá từng món **chưa bao gồm thuế**. Để kiểm tra, mình tìm điều khoản bán hàng của Five Guys UK.

Tại [mục 2.3 trên trang Legal](https://www.fiveguys.co.uk/legal/), Five Guys ghi rõ:

> “Prices will be as quoted on this Website. These prices include VAT.”

Giá niêm yết đã có VAT. Vì vậy, cộng thêm 20% sẽ tính thuế lần thứ hai. Tổng tiền bao gồm VAT vẫn là:

```text
£8.65 + £8.65 + £4.25 = £21.55
```

## Flag

```text
cdctf{£21.55}
```

Bài này chủ yếu kiểm tra một giả định rất dễ bỏ qua: **giá đang đọc đã gồm thuế hay chưa?** Phép cộng thì không khó; phần OSINT là tìm bằng chứng để biết mình có cần cộng thêm gì không.

*Ghi chú: `£25.86` đã được xác nhận là sai; trong cuộc trao đổi hiện tại chưa có phản hồi hệ thống chấm cho `£21.55`.*

---

Player

Hãy viết để tui paste vào file readme.md

---

Assistant

````markdown
# Value-Added Tax — cdCTF

- **Category:** OSINT
- **Points:** 500
- **Flag đề xuất:** `cdctf{£21.55}`

## Đề bài

Đề cung cấp ảnh một hóa đơn bị rách và yêu cầu tìm tổng số tiền người mua đã thanh toán, bao gồm VAT.

Format flag:

```text
cdctf{[CurrencySymbol]XX.XX}
```

## Phân tích hóa đơn

Phần tổng tiền bị mất, nhưng vẫn đọc được tên cửa hàng và địa chỉ:

```text
FIVE GUYS BURGERS AND FRIES
13–15 Magdalen Street
```

Đây là chi nhánh Five Guys tại Oxford, Anh, nên đơn vị tiền tệ là bảng Anh (`£`).

Các món trên hóa đơn:

| Món | Giá |
| --- | ---: |
| Little Cheeseburger | £8.65 |
| Little Cheeseburger | £8.65 |
| Little Fries | £4.25 |

Dòng `ALL THE WAY` bên dưới mỗi burger là lựa chọn topping, không phải món tính tiền riêng.

Tổng giá các món:

```text
8.65 + 8.65 + 4.25 = £21.55
```

## Cái bẫy VAT

Ban đầu, thấy đề hỏi số tiền “plus VAT”, mình cộng thêm thuế VAT 20%:

```text
21.55 × 1.20 = £25.86
```

Nhưng flag `cdctf{£25.86}` bị từ chối.

> Mình: Cộng tiền rồi thêm VAT, bài này dễ.
>
> Hệ thống: Incorrect.
>
> Mình: Khoan đã…

Điểm cần kiểm tra là giá trên hóa đơn đã bao gồm VAT hay chưa.

Trong [điều khoản chính thức của Five Guys UK](https://www.fiveguys.co.uk/legal/), mục **2.3** ghi:

> Prices will be as quoted on this Website. These prices include VAT.

Như vậy, giá niêm yết đã bao gồm VAT. Cộng thêm 20% sẽ tính thuế lần thứ hai.

Từ đó, tổng thanh toán được suy ra là:

```text
£8.65 + £8.65 + £4.25 = £21.55
```

## Flag đề xuất

```text
cdctf{£21.55}
```

**Trạng thái:** `£25.86` đã bị hệ thống từ chối. Flag `£21.55` được suy ra từ thông tin trên hóa đơn và điều khoản Five Guys, nhưng chưa có xác nhận accepted.

## Bài học

Phần khó của bài không nằm ở phép cộng mà ở giả định về thuế. Trước khi cộng VAT, cần kiểm tra giá được đưa ra đã bao gồm VAT hay chưa.
````

---

Player

Viết bằng tiếng anh và chèn ảnh bài cho nữa

---

Assistant

Paste the Markdown below into `README.md`. The image path assumes your README is in `D:\ctf\cdCTF\VAT\`.

````markdown
# Value-Added Tax — cdCTF Write-up

- **Category:** OSINT
- **Points:** 500

## The Challenge

We are given a torn receipt and asked to work out the total amount the customer paid, including VAT.

The flag format is:

```text
cdctf{[CurrencySymbol]XX.XX}
```

!Receipt provided with the challenge

The bottom of the receipt is missing, taking the total with it. Luckily, the restaurant details and individual item prices are still visible.

## Reading the Receipt

The receipt identifies the restaurant as:

```text
FIVE GUYS BURGERS AND FRIES
13–15 Magdalen Street
14/07/2024
```

This points to Five Guys in Oxford, UK, so the currency is pounds sterling (`£`).

The visible items are:

| Item | Price |
| --- | ---: |
| Little Cheeseburger | £8.65 |
| Little Cheeseburger | £8.65 |
| Little Fries | £4.25 |

The `ALL THE WAY` lines describe the burger toppings rather than additional purchases.

Adding the three prices gives:

```text
8.65 + 8.65 + 4.25 = £21.55
```

## The VAT Trap

My first instinct was to add 20% VAT:

```text
21.55 × 1.20 = £25.86
```

I tried `cdctf{£25.86}`, but it was rejected.

> Me: Three items, a calculator, and 20% VAT. Easy.
>
> CTF platform: Incorrect.
>
> Me: Time to read the small print.

The calculation was fine. The assumption behind it needed checking: **did those prices already include VAT?**

I checked the [official Five Guys UK terms](https://www.fiveguys.co.uk/legal/). Section **2.3** states:

> Prices will be as quoted on this Website. These prices include VAT.

That supports treating the listed prices as VAT-inclusive. Adding another 20% would count the tax twice.

The resulting total is therefore:

```text
£8.65 + £8.65 + £4.25 = £21.55
```

## Proposed Flag

```text
cdctf{£21.55}
```

**Validation status:** The £25.86 submission was rejected. The £21.55 answer follows from the receipt and the VAT-inclusive pricing evidence, but acceptance has not yet been confirmed.

## Takeaway

Before adding tax, check whether it is already included. In this challenge, the useful OSINT step was finding the restaurant’s pricing terms.
````

---

Player

D:\ctf\cdCTF\VAT\Value-Added Tax đây là đường dẫn của ảnh

---

Assistant

Nếu `README.md` nằm cùng thư mục `D:\ctf\cdCTF\VAT\Value-Added Tax` với ảnh, dùng:

```markdown
!Challenge receipt
```

Thay dòng ảnh trong write-up bằng dòng trên.
