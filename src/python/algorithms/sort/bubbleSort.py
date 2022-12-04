def swap(vector, a, b):
    aux = vector[a]
    vector[a] = vector[b]
    vector[b] = aux


def sort(vector, max):
    if max > 1:
        for j in range(2, max + 1):
            if vector[j - 1] > vector[j]:
                swap(vector, j - 1, j)
        sort(vector, max - 1)


def main():
    vector = [3, 2, 4, 10, 8]
    print(vector)
    sort(vector, len(vector) - 1)
    print(vector)


main()
