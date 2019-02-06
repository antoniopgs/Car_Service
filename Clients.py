def read_clients():
    client_list = {}
    with open("Clients.txt", "r") as file:
        pre_client_list = file.readlines()
        for line in pre_client_list:
            if line == "":
                pass
            else:
                client = line.split(" ")
                username = client[0]
                pre_password = client[1]
                password = pre_password.strip("\n")
                client_list.update({username: password})
        return client_list


clients = read_clients()


def check_originality():
    originality = False
    while originality == False:
        a = input("Insert your new username: ")
        if len(a) == 0 or a == "admin":
            print("Invalid username.\n")
        elif a in clients:
            print("Username is taken.\n")
        else:
            originality = True
            return a


def validate_password():
    password_validity = False
    while password_validity == False:
        b = input("""Passwords must contain at least:
- 6 Characters
- 1 Upper Case Letter
- 1 Number
- 1 Special Character (!, #, $, %, &, /, (, ), =, ?, *, -, _, <, >)

Insert your new password: """)
        special_characters = ["!", "#", "$", "%", "&", "/", "(", ")", "=", "?", "*", "-", "_", "<", ">"]
        if len(b) >= 6 and any(x.isupper() for x in b) and any(x.isdigit() for x in b)\
                and len(list(set(special_characters).intersection(b))) > 0:
            password_validity = True
            return b
        else:
            print("Invalid Password.\n")


def create_account():
    with open("Clients.txt", "a+") as file:
        new_username = check_originality()
        new_password = validate_password()
        file.write(f"{new_username} {new_password}\n")
        print(f"\nACCOUNT SUCCESSFULLY CREATED\nHello {new_username}!")


def login():
    login_attempts_left = 3
    while login_attempts_left > 0:
        print("\nLogin Attempts Remaining: " + str(login_attempts_left))
        input_user = input("Insert your username: ")
        input_pass = input("Insert your password: ")
        if input_user in clients:
            if clients[input_user] == input_pass:
                login = True
                print(f"\nHello {input_user}!")
                if input_user == "admin":
                    return "admin"
                else:
                    return "client"
            else:
                print("Wrong password.\n")
                login_attempts_left -= 1
        else:
            print("Wrong Username.\n")
            login_attempts_left -= 1
    print("You exceeded the number of allowed login attempts.")
    quit()


def search_clients():
    for x in clients:
        print(f"USERNAME: {x} PASSWORD: {clients[x]}")
