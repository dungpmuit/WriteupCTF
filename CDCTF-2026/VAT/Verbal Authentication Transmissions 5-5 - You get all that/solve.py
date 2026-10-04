from pathlib import Path
import re

VOWELS = "aeiouy"
CONSONANTS = "bcdfghklmnprstvzx"


def decode(encoded):
    body = encoded.replace("-", "")[1:-1]
    seed = 1
    result = bytearray()

    def first_byte(chunk, seed):
        high = (VOWELS.index(chunk[0]) - seed % 6) % 6
        middle = CONSONANTS.index(chunk[1])
        low = (VOWELS.index(chunk[2]) - seed // 6) % 6
        if high > 3 or low > 3 or middle > 15:
            raise ValueError("Invalid Bubble Babble block")
        return (high << 6) | (middle << 2) | low

    for offset in range(0, len(body) - 3, 5):
        chunk = body[offset:offset + 5]
        a = first_byte(chunk, seed)
        high = CONSONANTS.index(chunk[3])
        low = CONSONANTS.index(chunk[4])
        if high > 15 or low > 15:
            raise ValueError("Invalid consonant")
        b = (high << 4) | low
        result.extend((a, b))
        seed = (seed * 5 + a * 7 + b) % 36

    tail = body[-3:]
    if tail[1] == "x":
        if tail != VOWELS[seed % 6] + "x" + VOWELS[seed // 6]:
            raise ValueError("Invalid checksum")
    else:
        result.append(first_byte(tail, seed))
    return bytes(result)


def encode(data):
    seed = 1
    result = "x"
    for offset in range(0, len(data), 2):
        a = data[offset]
        result += VOWELS[(((a >> 6) & 3) + seed) % 6]
        result += CONSONANTS[(a >> 2) & 15]
        result += VOWELS[((a & 3) + seed // 6) % 6]
        if offset + 1 < len(data):
            b = data[offset + 1]
            result += CONSONANTS[b >> 4] + "-" + CONSONANTS[b & 15]
            seed = (seed * 5 + a * 7 + b) % 36
    if len(data) % 2 == 0:
        result += VOWELS[seed % 6] + "x" + VOWELS[seed // 6]
    return result + "x"


if __name__ == "__main__":
    path = Path(__file__).parent / "attachments" / "cred_call_transcript.txt"
    transcript = path.read_text(encoding="utf-8-sig")
    credential = transcript.split("transmission:", 1)[1]
    encoded = "-".join(re.findall(r"[a-z]{5}", credential.lower()))
    flag = decode(encoded)
    if encode(flag) != encoded:
        raise ValueError("Re-encoding did not match the transcript")
    print(flag.decode("ascii"))
    print("Verified: re-encoding matches the original credential.")
