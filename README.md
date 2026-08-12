# Pure Python AES-128 Encryption Engine (From Scratch)

A step-by-step, pure Python implementation of the **Advanced Encryption Standard (AES-128)** built without external cryptographic libraries. 

This project explicitly demonstrates every stage of the AES block cipher pipeline, matching standard NIST test vectors and PKCS7-padded outputs from online crypto tools.

## 🚀 Features
- **Key Expansion:** Dynamic 10-round key derivation using S-Box substitution, cyclic shifts (`RotWord`), and round constants (`Rcon`).
- **Core State Transformations:**
  - `SubBytes` (Non-linear byte substitution using S-Box)
  - `ShiftRows` (Cyclic row permutations)
  - `MixColumns` (Galois Field $GF(2^8)$ matrix multiplication)
  - `AddRoundKey` (Bitwise XOR with round keys)
- **Output Formats:** Column-major state matrix conversion to Hex and Base64.

## 🛠️ Project Structure
- `AES.py`: Main encryption pipeline runner.
- `AddRoundKey.py`: Implements Key Expansion algorithm and XOR state blending.
- `SubBytes.py`: Non-linear $S$-Box byte substitutions.
- `ShiftRow.py`: Cyclic row shifts.
- `MixColumns.py`: Galois Field $GF(2^8)$ arithmetic.
- `ConvertText.py`: State matrix to Hex and Base64 string converter.

## 💻 How to Run
```bash
python AES.py
