text = 'Hello AES Cipher'

array2 = [
    [], 
    [], 
    [], 
    []
]

arrayhex = [
    [], 
    [], 
    [], 
    []
]
arraytext = [
    [], 
    [], 
    [], 
    []
]

x=0
for i in text:
    array2[x].append(i)
    x += 1
    if x == 4:
        x = 0

y=0
for i in array2:
    for char in i:
        arrayhex[y].append(char.encode("utf-8").hex())
    y += 1
    if y == 4:
        y = 0

for row in arrayhex:
    print(row)

z=0
for i in arrayhex:
    for char in i:
        arraytext[z].append(bytes.fromhex(char).decode("utf-8"))
    z += 1
    if z == 4:
        z = 0

for row in arraytext:
    print(row)
