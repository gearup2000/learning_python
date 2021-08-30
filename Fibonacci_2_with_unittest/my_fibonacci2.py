def fib(n):
    """
        Function calculate Fibonacci number from given n.

        Show exception TypeError, if not integer type was called.
        Show exception ValueError, if negative integer type or acceptable number was called.
        :param n: integer number from 0 to 999
        :return: integer number from 0 to ...
        >>> fib(1)
        1
        >>> fib(2)
        1
        >>> fib(3)
        2
        >>> fib(5)
        5
        >>> fib(10)
        55
        >>> fib(20)
        6765
        """
    if not isinstance(n, int):
        raise TypeError("Fibonacci function can work only with <class 'int'> type.")
    if n < 0:
        raise ValueError("Cannot use negative numbers for Fibonacci function.")
    if n >= 10000:
        raise ValueError("This function cannot work with numbers greater than 9999.")
    if n == 0:
        return 0
    f_2 = 0
    f_1 = 1
    for i in range(2, n + 1):
        f_1, f_2 = (f_1 + f_2), f_1
    return f_1


if __name__ == "__main__":
    import doctest
    doctest.testmod()
