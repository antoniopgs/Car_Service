from Clients import *
from Vehicles import *

print("Hello!\n")
cycle = True
while cycle:
    user_input = input("""--- MENU ---
1 - Login
2 - Create Account
3 - Quit

Insert command: """)
    if user_input == "1":
        cycle = False
        if login() == "admin":
            admin_cycle = True
            while admin_cycle:
                admin_input = input("""
--- MENU ---
1 - Add vehicle
2 - Change vehicle status
3 - Search vehicle
4 - Search clients
5 - Request vehicle
6 - Refresh
7 - Quit

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
                    refresh()
                elif admin_input == "7":
                    admin_cycle = False
                else:
                    print("Invalid command.\n")
        else:
            client_cycle = True
            while client_cycle:
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
        while client_cycle:
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
    elif user_input == "3":
        cycle = False
    else:
        print("Invalid command.\n")
