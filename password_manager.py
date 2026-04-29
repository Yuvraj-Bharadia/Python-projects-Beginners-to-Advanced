from cryptography.fernet import Fernet

'''
def write_key():
    key  = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)'''

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


key = load_key()
fer = Fernet(key)

def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = (line.rstrip())
            user, passw = data.split("|")
            print("User: ", user, ", Password: ", 
                    fer.decrypt(passw.encode()).decode())

def add():
    name = input("Account name: ")
    pwd = input("Password: ")

    with open("passwords.txt", "a") as f:
        f.write(name + " | " + (fer.encrypt(pwd.encode())).decode() + "\n")

master_pwd = input("What is the master password: ")

if master_pwd == "vyuvi":
    while True:
        mode = input("Would you like to add a new password or veiw existing ones, press q to quit the program (veiw/add/q)? ")
        if mode == "q":
            break

        if mode == "view":
            master_password = input("What is the view master password? ")
            if master_password == "yuvi":
                view()
        elif mode == "add":
            add()
        else:
            print("invalid mode.")
            continue
else:
    print("Get lost you hacker!")
    quit()