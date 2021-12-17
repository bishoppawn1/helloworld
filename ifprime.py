number = int(input("Type a number to check if it is a prime."))
count = 1

while (count < number):
    count += 1
    if float(number) != int(number):
        print(str(number) + " is not a prime number!")
        break

if count == number:
    print(str(number) + " is a prime number.")
