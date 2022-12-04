def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def main():
    # print factorial from 1 to 10
    for n in range(1, 11):
        print(f'Fatorial of {n}: {factorial(n)}')


main()
