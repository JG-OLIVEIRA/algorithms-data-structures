def torneio(m):
    if m == 2:
        tabela[0][0] = 1
        tabela[0][1] = 2
        tabela[1][0] = 2
        tabela[1][1] = 1
        return tabela
    elif(m % 2 != 0):
        torneio(m + 1)
    else:
        p = m//2
        torneio(p)
        for i in range(0,p):
            for j in range(0,p):
                tabela[i+p][j] = tabela[i][j] + p
                tabela[i][j+p] = m - (j - i + m) % p 
                tabela[(m - (j - i + m) % p) - 1][j+p] = i + 1
        return tabela

def gera_bye():
    for i in range(0, m):
            for j in range(0, m):
                if(tabela[i][j] == m + 1):
                    tabela[i][j] = 0

def cria_matriz(m):
    matriz = []
    for i in range(m):
        linha = []
        for j in range(m):
            linha.append(0)
        matriz.append(linha)
    return matriz

def imprime_matriz(m):
    for i in range(m):
        for j in range(m):
            print(tabela[i][j], end = " ")
        print("")

#testando para casos de 2 até 14
for i in range(2, 14):
    m = i
    if(m % 2 == 0):
        tabela = cria_matriz(m)
        torneio(m)
        imprime_matriz(m)
        print("\n")
    else:
        tabela = cria_matriz(m + 1)
        torneio(m + 1)
        imprime_matriz(m)
        print("\n")