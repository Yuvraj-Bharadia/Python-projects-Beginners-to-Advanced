from prettytable import PrettyTable

print("\nMy TO-DO List")

instructions = ("\n1: Enter A or a to add-new TO-DO\n2: Enter D or d to delete TO-DO\n3: Enter U or u to update TO-DO\n4: Enter E or e to exit the program\n5: Enter L or l to view your TO-DO List")
print(instructions)

my_todo_list = []

x = PrettyTable()

def my_list():
    x.field_names = ["Item Names"]
    for i in my_todo_list:
        x.add_row([i])
    print(x.get_string(title = "TO DO List"))
    x.clear_rows()


running = True
while running:
    user_input = input("What would you want to do? (A , D , U , E , L): ").lower()
    if user_input == "a":

        new_todo = input("\nPlease Enter your new TODO: ").lower()
        print(f"You current TODO is {new_todo}.")

        my_todo_list.append(new_todo)

    elif user_input == "d":
        while True:
            try:
                item_name = input("\nPlease Enter the name of the TODO that you want to delete: ").lower()
                if item_name in my_todo_list:
                    choice = input(f"\nAre you sure that you want to delete {item_name} from your TO-DO list (Y/N): ").lower()

                    if choice == "y" or choice == "yes":

                        my_todo_list.remove(item_name)

                        print("Your Update TODO list.")

                        my_list()

                        break
                else:
                    print("Item not Found!")

            except Exception:
                print("Something went Wrong!!!")

    elif user_input == "u":
        while True:

            item_name = input("\nPlease Enter the name of the TODO that you want to update: ").lower()

            try:
                if item_name in my_todo_list:

                    choice = input(f"\nAre you sure you want to update {item_name} in your TO-DO list (Y/N): ").lower()

                    if choice == "y":
                        update_item = input(f"Enter the name you want to update {item_name} with: ").lower()

                        index = my_todo_list.index(item_name)

                        my_todo_list[index] = update_item
                        
                        print("Your updated TO-DO List.")
                        my_list()

                        break
                else:
                    print("Item Not found!!!")

            except Exception:
                print("Something Went Wrong!!")

    elif user_input == "e":
        ask_user = input("\nAre you sure you want to exit (Y/N): ").lower()

        if ask_user == "y":
            running = False

    elif user_input == "l":
        my_list()

    elif user_input == "" or user_input == " ":
        print("Please enter something!")

    else:
        print("Please enter a valid Value!")