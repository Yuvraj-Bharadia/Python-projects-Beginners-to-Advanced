import random
import time

print("Welcome to this Hangman game, You will have 6 chances to guess the word!")
name = input("what is your name? ")
time.sleep(2)
play = input("Do you want to play the game? ")
if play == "yes":
    print("Hello", name, "Lets play Hangman")
    def main():
        global count
        global display
        global word
        global aldready_guessed
        global length
        global play_game
        words_to_guess = ["fortnite" , "memes", "dog", "cat", "chair", "tree", "red", "blue", "table", "science", "math", "computer", "phone"]
        word = random.choice(words_to_guess)
        length = len(word)
        count = 0
        display = "_" * length
        aldready_guessed = []
        play_game = ""


    def play_loop():
        global play_game
        play_game = input("Do you want to play again(y for yes and n for no): ")
        while play_game not in ["y", "Y", "n", "N"]:
            play_game = input("Do you want to play again(y for yes and n for no): ")

        if play_game == "y" or play_game == "Y":
            main()
            hangman()
        elif play_game == "n" or play_game == "N":
            print("Thanks for playing")
            exit()

    def hangman():
        global count
        global display
        global word
        global aldready_guessed
        global play_game
        limit = 6
        guess = input("This is the Hangman word:  " + display + " Enter your guess\n")
        guess = guess.strip()

        if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
            print("Invalid Input, Try again!")
            hangman()
        
        elif guess in word:
            while guess in word:
                aldready_guessed.append(guess)
                index = word.find(guess)
                word = word[:index] + "_" + word[index + 1:]
                display = display[:index] + guess + display[index + 1:]
            print(display + "\n")

        elif guess in aldready_guessed:
            print("Aldready guessed, Try another letter")
        
        else:
            count += 1

            time.sleep(1)

            if(count == 0):
                print("\n+---+")
                print("     |")
                print("     |")
                print("     |")
                print("   ===")

                print("Wrong letter " + str(limit - count) + " guesses left")

            elif(count == 1):
                print("\n+---+")
                print("O    |")
                print("     |")
                print("     |")
                print("   ===")

                print("Wrong letter " + str(limit - count) + " guesses left")

            elif(count == 2):
                print("\n+---+")
                print("O    |")
                print("|    |")
                print("     |")
                print("   ===")

                print("Wrong letter " + str(limit - count) + " guesses left")

            elif(count == 3):
                print("\n+---+")
                print(" O   |")
                print("/|   |")
                print("     |")
                print("   ===")

                print("Wrong letter " + str(limit - count) + " guesses left")

            elif(count == 4):
                print("\n+---+")
                print(" O   |")
                print("/|\  |")
                print("     |")
                print("   ===")

                print("Wrong letter " + str(limit - count) + " guesses left")

            elif(count == 5):
                print("\n+---+")
                print(" O   |")
                print("/|\  |")
                print("/    |")
                print("   ===")

                print("Wrong letter " + str(limit - count) + " guesses left")

            elif(count == 6): 
                print("\n+---+")
                print(" O   |")
                print("/|\  |")
                print("/ \  |")
                print("   ===")

                print("Wrong letter, You are hanged + you Lose + L boso")
                print()
                print("The word was" , word)
                print()
                print("The letters you guessed were" , aldready_guessed)
                print()
                play_loop()
        
        if word == "_" * length:
            print("You won you are not a loser, not L boso")
            print()
            play_loop()
        
        elif count != limit:
            hangman()
    main()
    hangman()

else:
    print("Ok bye")
    exit()