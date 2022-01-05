def check_value(m, i, j, value):
    for it in range(9):
        if m[i][it]== value:
            return False
        if m[it][j]== value:
            return False
    it = i//3
    jt = j//3
    for i in range(it * 3, it * 3 + 3):
        for j in range (jt * 3, jt * 3 + 3):
            if m[i][j]== value:
                return False
    return True