score = 0

print("Welcome to my computer quiz")

playing = input("Do you want to play? ").lower()

if playing != "yes":
    quit()

print("Okay! Let's Play, You have to get a score of at least 7 out of the 10 questions to live, you get a point when you get a question right and you lose a point when you get a question wrong :)    --------------------------------------------------------------------------------------")

answer = input("What does CPU stand for? ").lower()

if answer == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    score -= 1

answer = input("What does GPU stand for? ").lower()

if answer == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    score -= 1

answer = input("What does RAM stand for ").lower()

if answer == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    score -= 1

answer = input("What does PSU stand for? ").lower()

if answer == "power supply":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    score -= 1

answer = input("What does SSD stand for? ").lower()

if answer == "solid state drive":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    score -= 1

answer = input("What does HDD stand for? ").lower()

if answer == "hard disk drive":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    score -= 1

answer = input("What does USB stand for? ").lower()

if answer == "universal serial bus":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    score -= 1

answer = input("What does CD stand for? ").lower()

if answer == "compact disk":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    score -= 1

answer = input("What does IMEI stand for? ").lower()

if answer == "international mobile equipment identity":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    score -= 1

answer = input("What does SIM stand for? ").lower()

if answer == "subscriber identity module":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    score -= 1

if score >= 7:
    print("You Won and got a score of:", score)
    quit()

else:
    print("You lost, learn and comeback!")