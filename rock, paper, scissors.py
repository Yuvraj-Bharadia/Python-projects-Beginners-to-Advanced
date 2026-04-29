import random
score = 0
chances = 0
while True:

    choices = ["rock", "paper", "scissors"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        print("Stop Joking around, give a rock, paper or a scissors")
        player = input("rock, paper, scissors: " ).lower()

    if player == computer:
        print('computer: ', computer)
        print("player: ", player)
        print("Tie!")
        chances += 1

    elif player == "rock":
        if computer == "paper":
                print('computer: ', computer)
                print("player: ", player)
                print("You lose!")
                chances += 1
        if score == 5:
            print(score, "You won!")
            break
        if chances == 15 and score != 5:
            print("You lose")
            break
        if computer == "scissors":
                print('computer: ', computer)
                print("player: ", player)
                print("You Win!")
                chances += 1
                score += 1
        if score == 5:
            print(score, "You won!")
            break
        if chances == 15 and score != 5:
            print("You lose")
            break

    elif player == "paper":
        if computer == "scissors":
                print('computer: ', computer)
                print("player: ", player)
                print("You lose!")
                chances += 1
        if score == 5:
            print(score, "You won!")
            break
        if chances == 15 and score != 5:
            print("You lose")
            break
        if computer == "rock":
                print('computer: ', computer)
                print("player: ", player)
                print("You Win!")
                chances += 1
                score += 1
        if score == 5:
            print(score, "You won!")
            break
        if chances == 15 and score != 5:
            print("You lose")
            break

    elif player == "scissors":
        if computer == "rock":
                print('computer: ', computer)
                print("player: ", player)
                print("You lose!")
                chances += 1
        if score == 5:
            print(score, "You won!")
            break
        if chances == 15 and score != 5:
            print("You lose")
            break
        if computer == "paper":
                print('computer: ', computer)
                print("player: ", player)
                print("You Win!")
                chances += 1
                score += 1
        if score == 5:
            print(score, "You won!")
            break
        if chances == 15 and score != 5:
            print("You lose")
            break

    play_again = input("Play Again (yes/no): ").lower()
    if play_again == "yes":
        continue
    elif play_again == "no":
        break
    else:
        play_again = input("Stop Joking, This is serious, do you want to play again (yes/no): ")
        if play_again == "yes":
            continue
        elif play_again == "no":
            break