# count_to = int(input("what number in the Fibonacci sequence do you want to go up to for example : 10 will count up to 55."))
current_num = 0


def fib(n):
    if (n == 0):
        return 0
    if (n == 1):
        return 1
    if (n == 2):
        return 1
    count = 0
    num1 = 0
    num2 = 1

    while (count < n):
        current_num = num1 + num2
        num1 = num2
        num2 = current_num
        count += 1
    return current_num
for i in range(110):
    print(str(i) + " : " + str(fib(i)))
