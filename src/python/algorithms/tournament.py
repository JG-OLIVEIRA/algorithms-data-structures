def tournament(mat, m):
    if m == 2:
        mat[0][0] = 1
        mat[0][1] = 2
        mat[1][0] = 2
        mat[1][1] = 1
        return mat
    elif m % 2 != 0:
        tournament(mat, m + 1)
    else:
        p = m // 2
        tournament(mat, p)
        for i in range(0, p):
            for j in range(0, p):
                mat[i + p][j] = mat[i][j] + p
                mat[i][j + p] = m - (j - i + m) % p
                mat[(m - (j - i + m) % p) - 1][j + p] = i + 1
        return mat


def generate_bye(mat, m):
    for i in range(0, m):
        for j in range(0, m):
            if mat[i][j] == m + 1:
                mat[i][j] = 0
    return mat


def create_linear_matrix(m, n):
    mat = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append(0)
        mat.append(row)
    return mat


def print_linear_matrix_formated(mat, m, n):
    for i in range(m):
        for j in range(n):
            print(mat[i][j], end=" ")
        print("")


def main():
    for m in range(2, 14):
        if m % 2 == 0:
            mat = create_linear_matrix(m, m)
            tournament(mat, m)
            print_linear_matrix_formated(mat, m, m)
            print("\n")
        else:
            mat = create_linear_matrix(m + 1, m + 1)
            tournament(mat, m)
            mat = generate_bye(mat, m)
            print_linear_matrix_formated(mat, m, m)
            print("\n")


main()
