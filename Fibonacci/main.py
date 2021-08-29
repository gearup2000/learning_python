import my_fibonacci


def main():
    n = int(input("Please enter the number for Fibonacci number: "))
    f = my_fibonacci.fib(n)
    print("Your Fibonacci number is: ", f)


if __name__ == "__main__":
    main()
