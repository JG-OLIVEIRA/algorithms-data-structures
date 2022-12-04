def merge(vector, left, middle, right):
    helper = [0] * len(vector)
    for i in range(left, right + 1):
        helper[i] = vector[i]

    i = left
    j = middle + 1
    k = left

    while i <= middle and j <= right:
        if helper[i] <= helper[j]:
            vector[k] = helper[i]
            i += 1
        else:
            vector[k] = helper[j]
            j += 1
        k += 1

    while i <= middle:
        vector[k] = helper[i]
        i += 1
        k += 1

    while j <= right:
        vector[k] = helper[j]
        j += 1
        k += 1


def sort(vector, left, right):
    if left < right:
        middle = (left+right)//2
        sort(vector, left, middle)
        sort(vector, middle + 1, right)
        merge(vector, left, middle, right)


def main():
    vector = [3, 2, 4, 10, 8]
    print(vector)
    sort(vector, 0, len(vector) - 1)
    print(vector)


main()
