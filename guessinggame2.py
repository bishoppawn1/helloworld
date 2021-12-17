import random
smallest = 0
largest = 10
answer = random.randint(smallest, largest - 1)
guess = 0
num_guesses = 0

def check():
    global guess
    global num_guesses
    guess = int(input("guess a number between " + str(smallest) + " and " + str(largest)))
    num_guesses += 1
    if guess == answer:
        print ("well done you got it! And here is how many guesses it took :" + str(num_guesses))
    elif guess > answer:
        print ("guess lower")
    elif guess < answer:
        print ("guess higher")

while guess > answer or guess < answer:
    check()


