from Clients import *
from Vehicles import *

print("Hello!\n")
cycle = True
while cycle == True:
    user_input = input("""--- MENU ---
1 - Login
2 - Create Account
3 - Quit

Insert command: """)
    if user_input == "1":
        cycle = False
        if login() == "admin":
            admin_cycle = True
            while admin_cycle == True:
                admin_input = input("""
--- MENU ---
1 - Add vehicle
2 - Change vehicle status
3 - Search vehicle
4 - Search clients
5 - Request vehicle
6 - Quit

Insert command: """)
                if admin_input == "1":
                    add()
                elif admin_input == "2":
                    change_status()
                elif admin_input == "3":
                    search_vehicles()
                elif admin_input == "4":
                    search_clients()
                elif admin_input == "5":
                    request()
                elif admin_input == "6":
                    admin_cycle = False
                else:
                    print("Invalid command.\n")
        else:
            client_cycle = True
            while client_cycle == True:
                client_input = input("""
--- MENU ---
1 - Request vehicle
2 - Quit

Insert command: """)
                if client_input == "1":
                    request()
                elif client_input == "2":
                    client_cycle = False
                else:
                    print("Invalid command.\n")
    elif user_input == "2":
        cycle = False
        create_account()
        client_cycle = True
        while client_cycle == True:
            client_input = input("""
--- MENU ---
1 - Request vehicle
2 - Quit

Insert command: """)
            if client_input == "1":
                client_x = input("Insert your x coordinate: ")
                client_y = input("Insert your y coordinate: ")
            elif client_input == "2":
                client_cycle = False
            else:
                print("Invalid command.\n")
    elif user_input == "3":
        cycle = False
    else:
        print("Invalid command.\n")
