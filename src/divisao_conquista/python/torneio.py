def tournament(m):
    if m == 2:
        matrix[0][0] = 1
        matrix[0][1] = 2
        matrix[1][0] = 2
        matrix[1][1] = 1
        return matrix
    elif m % 2 != 0:
        tornoment(m + 1)
    else:
        p = m // 2
        tornoment(p)
        for i in range(0, p):
            for j in range(0, p):
                matrix[i + p][j] = matrix[i][j] + p
                matrix[i][j + p] = m - (j - i + m) % p
                matrix[(m - (j - i + m) % p) - 1][j + p] = i + 1
        return matrix


def gera_bye():
    for i in range(0, m):
        for j in range(0, m):
            if matrix[i][j] == m + 1:
                matrix[i][j] = 0


def create_matrix(m):
    matrix = []
    for i in range(m):
        linha = []
        for j in range(m):
            linha.append(0)
        matrix.append(linha)
    return matrix


def print_matrix(m):
    for i in range(m):
        for j in range(m):
            print(matrix[i][j], end=" ")
        print("")


for i in range(2, 14):
    m = i
    if m % 2 == 0:
        matrix = create_matrix(m)
        tornoment(m)
        print_matrix(m)
        print("\n")
    else:
        matrix = create_matrix(m + 1)
        tornoment(m + 1)
        print_matrix(m)
        print("\n")
