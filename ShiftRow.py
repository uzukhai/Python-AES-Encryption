def SR(arrayhex):
    row0, row1, row2, row3 = [row for row in arrayhex]

    col0, col1, col2, col3 = [col for col in row1]
    col0, col1, col2, col3 = col1, col2, col3, col0
    row1 = [col0, col1, col2, col3]

    col0, col1, col2, col3 = [col for col in row2]
    col0, col1, col2, col3 = col2, col3, col0, col1
    row2 = [col0, col1, col2, col3]

    col0, col1, col2, col3 = [col for col in row3]
    col0, col1, col2, col3 = col3, col0, col1, col2
    row3 = [col0, col1, col2, col3]

    result = [row0, row1, row2, row3]
    return result

