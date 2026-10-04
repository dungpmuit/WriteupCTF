# Original Chat Notes

These notes are preserved evidence from the solve session. Some attempts may be wrong; the README is the cleaned writeup.

Player

tìm flag ctf

---

Assistant

Flag là:

```text
cdctf{8u88l3_848813_fl4g_pa55ing}
```

Chuỗi trong transcript dùng mã hóa [Bubble Babble](https://pypi.org/project/bubblepy/). Mình đã giải mã và mã hóa ngược lại, kết quả khớp hoàn toàn với chuỗi gốc.

---

Player

Viết writeup bằng tiếng anh cho tôi, hãy viết giống con người và có thể chèn meme vào

---

Assistant

# Verbal Authentication Transmissions 5/5: You Get All That?

**Category:** OSINT / Crypto  
**Points:** 500

## The challenge

We were given a captured automated phone call and a transcript. The message claimed to contain a shared credential from Jeffery Barrett, encoded “for ease of verbal transmission.”

The credential sounded like this:

```text
ximok. gemul. ganol. ruvul. hevaf. murof. felyf. metuf.
myvaf. cusih. zynok. sitek. lulol. bemef. hatok. norek. lizyx.
```

Apparently, “ease of verbal transmission” means making the receiver sound like they’re summoning something.

> **Automated voice:** “You get all that?”  
> **Me:** “I understood approximately zero words.”

Luckily, the transcript saved us from replaying the audio until those syllables became permanent residents in our heads.

## Recognizing the encoding

The useful clue was the shape of the text. Every spoken group had five letters, with alternating vowels and consonants. The entire sequence also started and ended with `x`.

That pointed to **Bubble Babble**, an encoding designed to turn binary data into pronounceable text. It uses these alphabets:

```python
vowels = "aeiouy"
consonants = "bcdfghklmnprstvzx"
```

Joining the spoken groups with hyphens gave us:

```text
ximok-gemul-ganol-ruvul-hevaf-murof-felyf-metuf-myvaf-cusih-zynok-sitek-lulol-bemef-hatok-norek-lizyx
```

One slightly confusing detail: the hyphens separate the *spoken groups*, but those groups are not independent blocks to decode. Bubble Babble carries a changing checksum state through the sequence.

## Decoding it

Bubble Babble begins with a seed of `1`. For each pair of bytes, the first byte is represented by a vowel–consonant–vowel sequence, and the second byte by two consonants. The vowel positions depend on the current seed.

After decoding each byte pair, the seed updates as:

```python
seed = (seed * 5 + first_byte * 7 + second_byte) % 36
```

Here is the Python decoder used for this challenge:

```python
VOWELS = "aeiouy"
CONSONANTS = "bcdfghklmnprstvzx"

encoded = (
    "ximok-gemul-ganol-ruvul-hevaf-murof-felyf-metuf-"
    "myvaf-cusih-zynok-sitek-lulol-bemef-hatok-norek-lizyx"
)

# Remove spoken separators and the outer 'x' markers.
body = encoded.replace("-", "")[1:-1]

seed = 1
decoded = bytearray()


def decode_first_byte(chunk, seed):
    high = (VOWELS.index(chunk[0]) - seed % 6) % 6
    middle = CONSONANTS.index(chunk[1])
    low = (VOWELS.index(chunk[2]) - seed // 6) % 6

    if high > 3 or low > 3 or middle > 15:
        raise ValueError("Invalid Bubble Babble block")

    return (high << 6) | (middle << 2) | low


# Each full block represents two bytes.
for offset in range(0, len(body) - 3, 5):
    chunk = body[offset:offset + 5]

    first = decode_first_byte(chunk, seed)
    second = (
        CONSONANTS.index(chunk[3]) << 4
    ) | CONSONANTS.index(chunk[4])

    decoded.extend([first, second])
    seed = (seed * 5 + first * 7 + second) % 36

# The final three letters encode one remaining byte,
# or contain the checksum terminator for even-length input.
tail = body[-3:]

if tail[1] == "x":
    expected = VOWELS[seed % 6] + "x" + VOWELS[seed // 6]
    if tail != expected:
        raise ValueError("Invalid checksum")
else:
    decoded.append(decode_first_byte(tail, seed))

print(decoded.decode("ascii"))
```

The output was:

```text
cdctf{8u88l3_848813_fl4g_pa55ing}
```

To verify the result, I encoded the decoded text back into Bubble Babble. It reproduced the original sequence exactly, including the final `lizyx`.

> **Me before decoding:** “This must be some elaborate cipher.”  
> **Me after decoding:** “The password was just speaking fluent bubble.”

## Flag

```text
cdctf{8u88l3_848813_fl4g_pa55ing}
```

---

Player

viết để tôi paste vô README.md

---

Assistant

````markdown
# Verbal Authentication Transmissions 5/5: You Get All That?

**Category:** OSINT / Crypto  
**Points:** 500

## Challenge Description

We intercepted an automated message sent to one of Jeffery Barrett’s employees at Crimson Clinic. The message contained a shared credential, but it was encoded in a strange way.

The challenge provided:

- `captured_cred_call.mp3`
- `cred_call_transcript.txt`

Flag format: `cdctf{ex4mp13_fl4g}`

## First Look

The transcript read:

> Hello User. You have. One. shared credential from. Jeffery. Barrett. Here is your credential, encoded for ease of verbal transmission: ximok. gemul. ganol. ruvul. hevaf. murof. felyf. metuf. myvaf. cusih. zynok. sitek. lulol. bemef. hatok. norek. lizyx.

“For ease of verbal transmission” was doing a lot of heavy lifting here.

> **Robot:** You get all that?  
> **Me:** Bro, you just cast a spell.

Fortunately, the transcript meant I could work directly with the text instead of repeatedly listening to the audio.

## Identifying the Encoding

The credential had a few useful characteristics:

- Every spoken group contained five letters.
- The letters followed a regular vowel/consonant pattern.
- The complete sequence started and ended with `x`.

These clues pointed to **Bubble Babble**, an encoding that represents binary data as pronounceable syllables.

It uses the following alphabets:

```python
vowels = "aeiouy"
consonants = "bcdfghklmnprstvzx"
```

Joining the spoken groups with hyphens produced:

```text
ximok-gemul-ganol-ruvul-hevaf-murof-felyf-metuf-myvaf-cusih-zynok-sitek-lulol-bemef-hatok-norek-lizyx
```

One detail matters here: the spoken groups are not independent encoded chunks. Bubble Babble carries a changing seed through the entire message.

## Decoding

The seed starts at `1`.

For each pair of bytes:

1. The first byte is represented by a vowel–consonant–vowel sequence.
2. The second byte is represented by two consonants.
3. The seed is updated using both decoded bytes:

```python
seed = (seed * 5 + first_byte * 7 + second_byte) % 36
```

The vowel positions depend on that seed, so decoding must proceed in order.

I used this Python script:

```python
VOWELS = "aeiouy"
CONSONANTS = "bcdfghklmnprstvzx"

encoded = (
    "ximok-gemul-ganol-ruvul-hevaf-murof-felyf-metuf-"
    "myvaf-cusih-zynok-sitek-lulol-bemef-hatok-norek-lizyx"
)

# Remove the hyphens and the outer x markers.
body = encoded.replace("-", "")[1:-1]

seed = 1
decoded = bytearray()


def decode_first_byte(chunk, seed):
    high = (VOWELS.index(chunk[0]) - seed % 6) % 6
    middle = CONSONANTS.index(chunk[1])
    low = (VOWELS.index(chunk[2]) - seed // 6) % 6

    if high > 3 or low > 3 or middle > 15:
        raise ValueError("Invalid Bubble Babble block")

    return (high << 6) | (middle << 2) | low


# Each full block contains two bytes.
for offset in range(0, len(body) - 3, 5):
    chunk = body[offset:offset + 5]

    first = decode_first_byte(chunk, seed)

    high = CONSONANTS.index(chunk[3])
    low = CONSONANTS.index(chunk[4])

    if high > 15 or low > 15:
        raise ValueError("Invalid consonant")

    second = (high << 4) | low

    decoded.extend([first, second])
    seed = (seed * 5 + first * 7 + second) % 36

# For odd-length input, the final three letters encode one byte.
# For even-length input, they contain a checksum terminator.
tail = body[-3:]

if tail[1] == "x":
    expected = VOWELS[seed % 6] + "x" + VOWELS[seed // 6]

    if tail != expected:
        raise ValueError("Invalid checksum")
else:
    decoded.append(decode_first_byte(tail, seed))

print(decoded.decode("ascii"))
```

Output:

```text
cdctf{8u88l3_848813_fl4g_pa55ing}
```

I also re-encoded the recovered flag into Bubble Babble. The result matched the original sequence exactly.

> **Before:** What ancient language is this?  
> **After:** Turns out the robot was just saying the flag with extra steps.

## Flag

```text
cdctf{8u88l3_848813_fl4g_pa55ing}
```

## Reference

- [Bubble Babble Python library and examples](https://pypi.org/project/bubblepy/)
````

---

Player

tôi có nên đính kèm những file đề cho vào writeup ko

---

Assistant

Có, **nên đính kèm các file đề bài nếu luật cuộc thi cho phép chia sẻ**, nhất là sau khi giải kết thúc. Người đọc sẽ có thể tự chạy lại cách giải của bạn.

Với bài này, nên thêm cả transcript và MP3 vào repo:

```text
verbal-authentication-5/
├── README.md
├── solve.py
└── attachments/
    ├── captured_cred_call.mp3
    └── cred_call_transcript.txt
```

Trong `README.md`, chèn:

```markdown
## Challenge Files

- Captured audio
- Call transcript
```

Transcript là file quan trọng nhất để tái hiện lời giải; MP3 giúp giữ đầy đủ ngữ cảnh đề bài. Nếu giải còn đang diễn ra, hãy kiểm tra quy định trước khi công khai writeup và flag.

---

Player

D:\ctf\cdCTF\VAT\Verbal Authentication Transmissions 55 You get all that
đây là thu mực chứa file

---

Assistant

Mình đã đặt writeup vào thư mục bạn đưa:

```text
Verbal Authentication Transmissions 55 You get all that/
├── README.md
├── solve.py
├── attachments/
│   ├── captured_cred_call.mp3
│   └── cred_call_transcript.txt
└── ... các file đề gốc
```

README viết bằng tiếng Anh, có meme dạng hội thoại và link tải file đề. Script đã chạy thành công, trả về đúng flag.

Bản sao: README.md.

---

Player

tôi muốn có 1 thư mục writeup riêng

---

Assistant

Đã gom vào thư mục `writeup/` riêng:

```text
Verbal Authentication Transmissions 55 You get all that/
├── captured_cred_call.mp3
├── cred_call_transcript.txt
└── writeup/
    ├── README.md
    ├── solve.py
    └── attachments/
        ├── captured_cred_call.mp3
        └── cred_call_transcript.txt
```

Các link trong README vẫn đúng và script đã chạy kiểm tra thành công.

---

Player

D:\ctf\WriteupCTF bổ sung vào nơi đây vì đây là folder viết Writeup của tôi

---

Assistant

Đã bổ sung vào:

```text
D:\ctf\WriteupCTF\CDCTF-2026\VAT\
└── Verbal Authentication Transmissions 5-5 - You get all that\
    ├── README.md
    ├── solve.py
    └── attachments\
        ├── captured_cred_call.mp3
        └── cred_call_transcript.txt
```

Mình giữ nội dung README hiện có, thêm link file đề và link bài vào README tổng. Script đã chạy thành công.

---

Player

Hãy chỉnh lại writeup cho đúng liên kết chưa

---

Assistant

Đã chỉnh lại writeup trong `D:\ctf\WriteupCTF`.

- Link từ README tổng đến bài viết đúng.
- Link đến MP3, transcript và `solve.py` đều trỏ tới file tồn tại.
- Đã thêm hướng dẫn chạy `python solve.py`.

Các liên kết dùng đường dẫn tương đối, nên vẫn hoạt động khi đưa thư mục lên GitHub.
