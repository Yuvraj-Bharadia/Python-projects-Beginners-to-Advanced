import random

top_of_range = (input("Type a Number: "))

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("please type in a number larger than 0 next time")
        quit()
else:
    print("please enter a number")
    quit()

random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a GUESS: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("please enter a number")
        continue

    if user_guess == random_number:
        print("You got it")
        break
    elif user_guess > random_number:
        print("You were above the number!")
    else:
        print("You were below the number!")

print("You got it in", guesses, "guesses")