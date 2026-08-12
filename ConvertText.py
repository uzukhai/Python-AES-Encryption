import base64

def CT(arrayhex):
    byte_list = []

    for col in range(4):
        for row in range(4):
            byte_val = int(arrayhex[row][col], 16)
            byte_list.append(byte_val)
            
    raw_bytes = bytes(byte_list)
    
    hex_string = raw_bytes.hex()
    base64_string = base64.b64encode(raw_bytes).decode('ascii')
    
    return hex_string, base64_string