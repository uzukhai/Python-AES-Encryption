# AES-128-From-Scratch (Pure Python)

A step-by-step implementation of the **Advanced Encryption Standard (AES-128)** written in pure Python without external libraries. 

This project demonstrates the exact mathematical transformations executed on a 128-bit (16-byte) block of data through all 10 rounds of AES.

## 📌 Features
- **Pure Python:** Built entirely using standard library functions.
- **Dynamic Key Expansion:** Derives 11 round keys (176 bytes) dynamically using `RotWord`, `SubWord`, and `Rcon`.
- **Full AES Pipeline:**
  - `SubBytes` (S-Box byte substitution)
  - `ShiftRows` (Cyclic row permutations)
  - `MixColumns` (Galois Field $GF(2^8)$ multiplication)
  - `AddRoundKey` (Bitwise XOR state blending)
- **Column-Major Conversion:** Formats the final $4 \times 4$ state matrix into standard Hex and Base64 outputs.

> **Note on Block Size & Padding:** 
> This implementation processes raw 128-bit (16-byte) blocks in ECB mode without automatic PKCS7 padding. 
> Inputs must be exactly 16 bytes (128 bits) in length.

## ⚙️ Usage Requirements
- Input text must be **exactly 16 bytes / 16 characters** (e.g., `'Hello AES Cipher'`).
- Secret key must be **exactly 16 bytes / 16 characters** (e.g., `'MySecretKey12345'`).

## 🚀 How to Run

```bash
python AES.py
