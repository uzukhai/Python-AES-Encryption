# Galois Field (GF 2^8) Multiplication by 2
def gmul2(x):
    return ((x << 1) ^ 0x1B) & 0xFF if (x & 0x80) else (x << 1) & 0xFF

# Galois Field Multiplication by 3 (which is (x * 2) ^ x)
def gmul3(x):
    return gmul2(x) ^ x

def MC(arrayhex):
    # Constant MixColumns Matrix
    GF = [
        [2, 3, 1, 1],
        [1, 2, 3, 1],
        [1, 1, 2, 3],
        [3, 1, 1, 2]
    ]

    result = [[], [], [], []]

    # Process column by column (MixColumns operates on state matrix columns)
    for c in range(4):
        # Extract column c as integer byte values
        col = [int(arrayhex[r][c], 16) for r in range(4)]

        # Multiply GF matrix by state column
        r0 = gmul2(col[0]) ^ gmul3(col[1]) ^ col[2]          ^ col[3]
        r1 = col[0]          ^ gmul2(col[1]) ^ gmul3(col[2]) ^ col[3]
        r2 = col[0]          ^ col[1]          ^ gmul2(col[2]) ^ gmul3(col[3])
        r3 = gmul3(col[0]) ^ col[1]          ^ col[2]          ^ gmul2(col[3])

        # Convert integers back to 2-digit hex strings and append to rows
        result[0].append(f'{r0:02x}')
        result[1].append(f'{r1:02x}')
        result[2].append(f'{r2:02x}')
        result[3].append(f'{r3:02x}')

    return result