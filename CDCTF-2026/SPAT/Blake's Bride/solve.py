import argparse
import hashlib
import struct
import re
from pathlib import Path


def extract_hashes(path):
    data = Path(path).read_bytes()
    if data[:8] != b'\x89PNG\r\n\x1a\n':
        raise ValueError('Not a PNG')
    pos = 8
    while pos + 12 <= len(data):
        length = struct.unpack('>I', data[pos:pos + 4])[0]
        kind = data[pos + 4:pos + 8]
        payload = data[pos + 8:pos + 8 + length]
        if kind == b'iTXt' and b'exif:UserComment' in payload:
            hashes = re.findall(rb'[0-9a-f]{128}', payload)
            if len(hashes) == 3:
                return [h.decode() for h in hashes]
        pos += length + 12
    raise ValueError('Could not find the three hashes in XMP UserComment')


def crack(hashes, wordlist):
    targets = {bytes.fromhex(h): i for i, h in enumerate(hashes)}
    found = [None] * len(hashes)
    for word in Path(wordlist).read_text(encoding='utf-8').split():
        base = hashlib.blake2b(word.encode())
        for number in range(1000):
            suffix = f'{number:03d}'
            candidate_hash = base.copy()
            candidate_hash.update(suffix.encode())
            index = targets.get(candidate_hash.digest())
            if index is not None:
                found[index] = word + suffix
                print(f'password{index + 1}: {found[index]}', flush=True)
                del targets[candidate_hash.digest()]
                if not targets:
                    return found
    return found


PASSWORDS = ['epithalamium738', 'trousseau201', 'honeymoon069']

def main():
    parser = argparse.ArgumentParser(description="Solve Blake's Bride")
    parser.add_argument('png', type=Path)
    parser.add_argument('--wordlist', type=Path, help='Optional dictionary to reproduce cracking')
    args = parser.parse_args()
    hashes = extract_hashes(args.png)
    for index, value in enumerate(hashes, 1):
        print(f'hash{index}: {value}')
    passwords = crack(hashes, args.wordlist) if args.wordlist else PASSWORDS
    if any(p is None for p in passwords):
        raise SystemExit('Wordlist did not recover all passwords')
    for password, target in zip(passwords, hashes):
        assert hashlib.blake2b(password.encode()).hexdigest() == target, password
    print('cdctf{' + '-'.join(passwords) + '}')


if __name__ == '__main__':
    main()

