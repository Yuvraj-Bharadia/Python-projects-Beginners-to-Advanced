
name = input("What is your name: ")#
print("Welcome", name, "to this adventure!")

answer = input(
    "You are on a dirt road, it has come to a dead end, you can go left or right. Which way would you want to go? "
).lower()

if answer == "left":
    answer = input("You come to a river, You can walk around it or swim across? type walk to walk around or swim to swim across the river: ").lower()
    if answer == "walk":
        answer = input("You meet a mysterious man who wont let you cross, he wants to ask you a math question. Do you want to fight through him or solve his math question and go free? (math/fight): ").lower()
        if answer == "fight":
            print("The man pulls out a gun and you lose!")
        elif answer == "math":
            answer == int(input("What is 5 + 4 x 3456 / 2? "))
            if answer == 34560:
                print("The man is impressed and they give you Gold. You Win!")
            else:
                print("You are bad at math, the man pulls out a gun and you lose!")
                quit()
        else:
            print("Not a valid option. You lose!")
            quit()
    elif answer == "swim":
        print("You chose to swim and you were eaten by a crocodile! Game Over!!")
        quit()
    else:
        print("This is not a valid option. You lose")
        quit()
elif answer == "right":
    answer = input("You come across a bridge and it looks wobbly, do you want to cross it or head back? (cross/back): ").lower()
    if answer == "back":
        answer = input("You are heading back, it is quite dark and you find a axe and it is glowing, do you want to take it or not? (yes/no): ").lower()
        if answer == "yes":
            print("The weapon was cursed and you burn your hand, you lose!")
            quit()
        elif answer == "no":
            print("You were running back to your dirt road and it was dark and you fell into a hole and you lost!")
            quit()
        else:
            print("Not a valid option, You lose")
            quit()
    elif answer == "cross":
        answer = input("You meet a stranger, do you talk to him or walk forward? (talk/forward): ").lower()
        if answer == "forward":
            print("The stranger is offended and you lose!")
            quit()
        elif answer == "talk":
            print("The stranger gives you 1$ and you move on")
            answer = input("You come to a store and you are thirsty, you are a few km away from your destination, do you want to buy water or keep walking to your destination? (walk/buy): ").lower()
            if answer == "walk":
                print("You died of thirst, you lose!")
                quit()
            elif answer == "buy":
                print("You spent your dollar and you drank water and you are now energized and you reach your destination easily. You win!")
                quit()
            else:
                print("Not a valid option, You lose")
                quit()
        else:
            print("Not a valid option, You lose")
            quit()
    else:
        print("Not a valid option, You lose")
        quit()
else:
    print("Not a valid option, You lose")
    quit()

print("Thank you for trying", name)