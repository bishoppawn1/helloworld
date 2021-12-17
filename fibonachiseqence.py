count_to = int(input("what number in the Fibonacci sequence do you want to go up to for example : 10 will count up to 55."))
count = 2
num1 = 1
num2 = 1
while(count < count_to):
    current_num = num1 + num2
    num1 = num2
    num2 = current_num
    count += 1

print(current_num)