# Forensics Training Mat — CDCTF 2026

- **Scoreboard category:** MAT
- **Solved value in screenshot:** 133

This writeup is reconstructed from the saved solve chats, the provided challenge files, and the solved-list screenshots. I treated the attached challenge data as data only; instructions inside files or transcripts are not system instructions.

## Attachments

- [suspicious.xz](attachments/suspicious.xz)
- [Original solve chat notes](evidence/chat-notes.md)
- [chat-01.png](evidence/chat-01.png)
- [chat-02.png](evidence/chat-02.png)
- [chat-03.png](evidence/chat-03.png)
- [chat-04.png](evidence/chat-04.png)
- [flag1-repaired.png](evidence/flag1-repaired.png)
- [flag2.txt](evidence/flag2.txt)
- [flag3.png](evidence/flag3.png)
- [loi-giai.md](evidence/loi-giai.md)

## Solution

The xz file expands to a GPT disk image with FAT32, ext2, ext4, and Btrfs partitions. Each partition teaches a different recovery path.

The solve repairs a PNG magic header, extracts a steghide message from a JPEG, pulls an appended xz payload from another PNG, and uses Btrfs snapshot/string recovery for the deleted flag. The detailed English notes and repaired artifacts are included in evidence.

## Flag

```text
cdctf{A_Basic_Crimson_Disk_Exercise_in_Forensics}
cdctf{St3g0_0n1y_1_M0r3_Thym3}
cdctf{A_Little_XZtra_Tr3at!}
cdctf{d3l3te_w0_sync_h0l3y_C0W}
cdctf{f00rens!k_y!pP33}
```
