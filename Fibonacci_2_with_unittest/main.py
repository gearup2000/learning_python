import my_fibonacci2


def main():
    n = int(input("Please enter the number for Fibonacci number: "))
    f = my_fibonacci2.fib(n)
    print("Your Fibonacci number is: ", f)


if __name__ == "__main__":
    main()
