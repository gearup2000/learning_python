import my_fibonacci

all_correct = True
for n, answer in [(0, 0), (1, 1), (2, 1), (5, 5), (10, 55)]:
    result = my_fibonacci.fib(n)
    correct = (result == answer)
    if not correct:
        print('Test case failed:', n, result, '!=', answer, )
    all_correct &= correct

if all_correct:
    print('Testing my_fibonacci: OK!')
else:
    print('Testing my_fibonacci: Failed!.')
