def main():
    number = int(input("Please enter the number of month: "))

    for i in range(1, number + 1):
        print(f'{i} month: {fibonacci(i)}')


def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


main()
