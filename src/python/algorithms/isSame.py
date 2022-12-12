def isSame(vector, begin, end):
    if (begin == end):
        return True
    if vector[begin] != vector[end]:
        return False
    middle = (begin + end)//2
    return isSame(vector, begin, middle) and isSame(vector, middle + 1, end)


def main():
    vector1 = [1, 1, 2, 2, 3, 4, 5]
    print('Input: ', vector1)
    print('Output: ', isSame(vector1, 0, len(vector1) - 1))
    print("There's different values")
    vector2 = [1, 1, 1, 1, 1, 1, 1]
    print('Input: ', vector2)
    print('Output: ', isSame(vector2, 0, len(vector2) - 1))
    print("All values are the same")


main()
