def findMajorityElement(vector, begin, end):
    # Caso base
    if begin == end:
        return vector[begin]

    # Divisão
    middle = (begin + end)//2
    left = findMajorityElement(vector, begin, middle)
    right = findMajorityElement(vector, middle + 1, end)

    # Conquista
    if left == right:
        return left
    if vector.count(left) > middle:
        return left
    if vector.count(right) > middle:
        return right


def main():
    vector = [4, 4, 2, 4, 7, 6, 4, 2, 4, 4, 7]
    print('Input:', vector)
    print('The length of vector:', len(vector))
    result = findMajorityElement(vector, 0, len(vector) - 1)
    print('The most frequency element:', result)


main()
