from HexTransform import *
from AddRoundKey import *
from SubBytes import *
from ShiftRow import *
from MixColumns import *
from ConvertText import *

text = 'Hello AES Cipher'
key = 'MySecretKey12345'

arrayhex = texttohex(text)
arraykey = texttohex(key)

arrayhex, arraykey = ARK(arrayhex, arraykey, 0)

for i in range(1, 10):
    arrayhex = SB(arrayhex)
    arrayhex = SR(arrayhex)
    arrayhex = MC(arrayhex)
    arrayhex, arraykey = ARK(arrayhex, arraykey, i)

arrayhex = SB(arrayhex)
arrayhex = SR(arrayhex)
arrayhex, arraykey = ARK(arrayhex, arraykey, 10)

arrayhex, arraybase64 = CT(arrayhex)

print(arrayhex)
print(arraybase64)
