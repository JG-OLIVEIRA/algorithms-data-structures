def sumSubset(set, begin, end, subset, result, x):
    if end <= x:
        if sum(subset) == x:
            print(subset)
        for i in range(begin, len(set)):
            sumSubset(set, i + 1, end + 1, subset + [set[i]], result, x)


def main():
    set = [i for i in range(1, 21)]
    sumSubset(set, 0, 1, [], [], 8)


main()
