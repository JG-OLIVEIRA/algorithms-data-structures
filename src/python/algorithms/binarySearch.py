def search(vector, key, begin, end):
    if begin <= end:
        middle = (begin + end) // 2
        if key == vector[middle]:
            return middle
        elif key < vector[middle]:
            return search(vector, key, begin, middle - 1)
        elif (key > vector[middle]):
            return search(vector, key, middle + 1, end)
    return -1


def main():
    vector = [3, 2, 4, 10, 8]
    print('Vector: ', vector)
    print('Input: ', 10)
    print('Output: ', search(vector, 10, 0, len(vector) - 1))
    print(
        f'The index of element {10} is {search(vector, 10, 0, len(vector) - 1)}')
    print('Input: ', 9)
    print('Output: ', search(vector, 9, 0, len(vector) - 1))
    print(
        f'The index of element {9} is {search(vector, 9, 0, len(vector) - 1)} because {9} there is not in array')


main()
