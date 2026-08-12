def texttohex(text):
    array2 = [[], [], [], []]
    arrayhex = [[], [], [], []]

    x = 0
    for i in text:
        array2[x].append(i)
        x += 1
        if x == 4:
            x = 0

    for row_idx, row in enumerate(array2):
        for char in row:
            arrayhex[row_idx].append(char.encode("utf-8").hex())

    return arrayhex