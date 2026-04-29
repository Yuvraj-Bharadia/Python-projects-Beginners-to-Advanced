from tkinter import *
from tkinter import messagebox
import random
import turtle

root = Tk()
root.title("Computers Paradise - Match Game.py")
#root.iconbitmap("file in here")
root.geometry("470x460")

global winner, matches, score
# Set winner counter to 0
winner = 0
score = 0
pen = turtle.Turtle()
pen.hideturtle()
pen.write(f"Player A = {score}", align = "center", font=("Courier", 24, "normal"))


# Create our matches
matches = [1,1,2,2,3,3,4,4,5,5,6,6]
# Shuffle our matches
random.shuffle(matches)

# Create button frame
my_frame = Frame(root)
my_frame.pack(pady=10)

# Define some variables
count = 0
answer_list = []
answer_dict = {}

# Create our reset Function
def reset():
    global winner, matches, score
    winner = 0
    score = 0
    # Create our matches
    matches = [1,1,2,2,3,3,4,4,5,5,6,6]
    # Shuffle our matches
    random.shuffle(matches)

    # Reset our labels
    my_label.config(text=" ")
    pen.clear()
    pen.write(f"Player A = {score}", align = "center", font=("Courier", 24, "normal"))

    # Reset our buttons
    button_list = [b0, b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11]
    # Loop through buttons and change colours
    for button in button_list:
        button.config(text= " ", bg= "SystemButtonFace", state="normal")

# Create winner function
def win():
    my_label.config(text= "Congratulations, You win")
    button_list = [b0, b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11]
    # Loop through buttons and change colours
    for button in button_list:
        button.config(bg= "yellow")

# Function for clicking buttons
def button_click(b, number):
    global count, answer_list, answer_dict, winner, score

    if b["text"] == " " and count < 2:
        b["text"] = matches[number]
        # Add number and button to answer list and answer dictionary
        answer_list.append(number)
        answer_dict[b] = matches[number]
        # Incremeant our counter
        count += 1

    # Determine correct or not
    if len(answer_list) == 2:
        if matches[answer_list[0]] == matches[answer_list[1]]:
            #my_label.config(text = "MATCH!")
            for key in answer_dict:
                key["state"] = "disabled"
            count = 0
            answer_dict = {}
            answer_list = []
            messagebox.showinfo("Correct Match!!", "correct")
            # Increment the winner counter
            winner += 1
            score += 1
            if winner == 6:
                win()

            pen.clear()
            pen.write(f"Player A = {score}", align = "center", font=("Courier", 24, "normal"))
        else:
            #my_label.config(text = "DOH!")
            count = 0
            answer_list = []
            # Pop up
            messagebox.showinfo("Incorrect!!!", "Incorrect")
            # Reset the buttons
            for key in answer_dict:
                key["text"] = " "

            pen.clear()
            pen.write(f"Player A = {score}", align = "center", font=("Courier", 24, "normal"))

            answer_dict = {}    



# Define our buttons
b0 = Button(my_frame, text=" ", font=("Helvetica", 20), height=3, width=6, command=lambda: button_click(b0, 0), relief="groove")
b1 = Button(my_frame, text=" ", font=("Helvetica", 20), height=3, width=6, command=lambda: button_click(b1, 1), relief="groove")
b2 = Button(my_frame, text=" ", font=("Helvetica", 20), height=3, width=6, command=lambda: button_click(b2, 2), relief="groove")
b3 = Button(my_frame, text=" ", font=("Helvetica", 20), height=3, width=6, command=lambda: button_click(b3, 3), relief="groove")
b4 = Button(my_frame, text=" ", font=("Helvetica", 20), height=3, width=6, command=lambda: button_click(b4, 4), relief="groove")
b5 = Button(my_frame, text=" ", font=("Helvetica", 20), height=3, width=6, command=lambda: button_click(b5, 5), relief="groove")
b6 = Button(my_frame, text=" ", font=("Helvetica", 20), height=3, width=6, command=lambda: button_click(b6, 6), relief="groove")
b7 = Button(my_frame, text=" ", font=("Helvetica", 20), height=3, width=6, command=lambda: button_click(b7, 7), relief="groove")
b8 = Button(my_frame, text=" ", font=("Helvetica", 20), height=3, width=6, command=lambda: button_click(b8, 8), relief="groove")
b9 = Button(my_frame, text=" ", font=("Helvetica", 20), height=3, width=6, command=lambda: button_click(b9, 9), relief="groove")
b10 = Button(my_frame, text=" ", font=("Helvetica", 20), height=3, width=6, command=lambda: button_click(b10, 10), relief="groove")
b11 = Button(my_frame, text=" ", font=("Helvetica", 20), height=3, width=6, command=lambda: button_click(b11, 11), relief="groove")

# Grid my Butttons
b0.grid(row=0, column=0)
b1.grid(row=0, column=1)
b2.grid(row=0, column=2)
b3.grid(row=0, column=3)

b4.grid(row=1, column=0)
b5.grid(row=1, column=1)
b6.grid(row=1, column=2)
b7.grid(row=1, column=3)

b8.grid(row=2, column=0)
b9.grid(row=2, column=1)
b10.grid(row=2, column=2)
b11.grid(row=2, column=3)

my_label = Label(root)
my_label.pack(pady=20)

# Create A Menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Create options dropdown menu
option_menu = Menu(my_menu, tearoff= False)
my_menu.add_cascade(label="Options", menu=option_menu)
option_menu.add_command(label="Reset Game", command=reset)
option_menu.add_separator()
option_menu.add_command(label="Exit Game", command=root.quit)

root.mainloop()