import math


def search_vehicles():
    cycle = True
    while cycle == True:
        a = input("""--- SEARCH OPTIONS ---
1 - Search all vehicles
2 - Search a specific vehicle

Insert command: """)
        if a == "1":
            cycle = False
            vehicle_list = []
            with open("Vehicles.txt", "r") as file:
                lines = file.readlines()
                for line in lines:
                    new_line = line.strip("\n")
                    print(new_line)
        elif a == "2":
            cycle = False
            cycle_2 = True
            while cycle_2 == True:
                b = input("""--- SEARCH BY ---
1 - ID
2 - License
3 - Manufacturer
4 - Model
5 - Driver
6 - Kilometers travelled
7 - Amount of trips
8 - Profit
9 - Type (car or van)
10 - Status

Insert command: """)
                if b == "1":
                    cycle_2 = False
                    c = input("Insert ID: ")
                    found_id = False
                    with open("Vehicles.txt", "r") as file:
                        lines = file.readlines()
                        for line in lines:
                            pre_id = line.split(" | ")
                            searched_id = pre_id[0]
                            if c in searched_id:
                                found_id = True
                                line_2 = line.strip("\n")
                                print(line_2)
                    if found_id == False:
                        print("No matching ID was found.\n")
                    else:
                        pass
                elif b == "2":
                    cycle_2 = False
                    c = input("Insert License: ")
                    found_license = False
                    with open("Vehicles.txt", "r") as file:
                        lines = file.readlines()
                        for line in lines:
                            pre_license = line.split(" | ")
                            searched_license = pre_license[1]
                            if c in searched_license:
                                found_license = True
                                line_2 = line.strip("\n")
                                print(line_2)
                    if found_license == False:
                        print("No matching License was found.\n")
                    else:
                        pass
                elif b == "3":
                    cycle_2 = False
                    c = input("Insert Manufacturer: ")
                    found_manufacturer = False
                    with open("Vehicles.txt", "r") as file:
                        lines = file.readlines()
                        for line in lines:
                            pre_manufacturer = line.split(" | ")
                            searched_manufacturer = pre_manufacturer[2]
                            if c in searched_manufacturer:
                                found_manufacturer = True
                                line_2 = line.strip("\n")
                                print(line_2)
                    if found_manufacturer == False:
                        print("No matching Manufacturer was found.\n")
                    else:
                        pass
                elif b == "4":
                    cycle_2 = False
                    c = input("Insert Model: ")
                    found_model = False
                    with open("Vehicles.txt", "r") as file:
                        lines = file.readlines()
                        for line in lines:
                            pre_model = line.split(" | ")
                            searched_model = pre_model[3]
                            if c in searched_model:
                                found_model = True
                                line_2 = line.strip("\n")
                                print(line_2)
                    if found_model == False:
                        print("No matching Model was found.\n")
                    else:
                        pass
                elif b == "5":
                    cycle_2 = False
                    c = input("Insert Driver: ")
                    found_driver = False
                    with open("Vehicles.txt", "r") as file:
                        lines = file.readlines()
                        for line in lines:
                            pre_driver = line.split(" | ")
                            searched_driver = pre_driver[4]
                            if c in searched_driver:
                                found_driver = True
                                line_2 = line.strip("\n")
                                print(line_2)
                    if found_driver == False:
                        print("No matching Driver was found.\n")
                elif b == "6":
                    cycle_2 = False
                    c = input("""--- VEHICLE KILOMETERS ---
Insert the amount of km: """)
                    d = input(f"""1 - Search for vehicles with {c} kilometers
2 - Search for vehicles with more than {c} kilometers
3 - Search for vehicles with less than {c} kilometers

Insert command: """)
                    found_kms = False
                    with open("Vehicles.txt", "r") as file:
                        lines = file.readlines()
                        for line in lines:
                            pre_kms = line.split(" | ")
                            searched_kms = pre_kms[5]
                            if d == "1" and int(searched_kms) == int(c):
                                found_kms = True
                                new_line = line.strip("\n")
                                print(new_line)
                            elif d == "2" and int(searched_kms) > int(c):
                                found_kms = True
                                new_line = line.strip("\n")
                                print(new_line)
                            elif d == "3" and int(searched_kms) < int(c):
                                found_kms = True
                                new_line = line.strip("\n")
                                print(new_line)
                        if d == "1" and found_kms == False:
                            print(f"No vehicles with {c} kilometers were found.\n")
                        elif d == "2" and found_kms == False:
                            print(f"No vehicles with more than {c} kilometers were found.\n")
                        elif d == "3" and found_kms == False:
                            print(f"No vehicles with less than {c} kilometers were found.\n")
                elif b == "7":
                    cycle_2 = False
                    c = input("""--- VEHICLE TRIPS ---
Insert the amount of trips: """)
                    d = input(f"""1 - Search for vehicles with {c} trips
2 - Search for vehicles with more than {c} trips
3 - Search for vehicles with less than {c} trips

Insert command: """)
                    found_trips = False
                    with open("Vehicles.txt", "r") as file:
                        lines = file.readlines()
                        for line in lines:
                            pre_trips = line.split(" | ")
                            searched_trips = pre_trips[6]
                            if d == "1" and int(searched_trips) == int(c):
                                found_trips = True
                                new_line = line.strip("\n")
                                print(new_line)
                            elif d == "2" and int(searched_trips) > int(c):
                                found_trips = True
                                new_line = line.strip("\n")
                                print(new_line)
                            elif d == "3" and int(searched_trips) < int(c):
                                found_trips = True
                                new_line = line.strip("\n")
                                print(new_line)
                        if d == "1" and found_trips == False:
                            print(f"No vehicles with {c} trips were found.\n")
                        elif d == "2" and found_trips == False:
                            print(f"No vehicles with more than {c} trips were found.\n")
                        elif d == "3" and found_trips == False:
                            print(f"No vehicles with less than {c} trips were found.\n")
                elif b == "8":
                    cycle_2 = False
                    c = input("""--- VEHICLE PROFIT ---
Insert the amount of profit: """)
                    d = input(f"""1 - Search for vehicles with a profit of {c}
2 - Search for vehicles with more than {c} profit
3 - Search for vehicles with less than {c} profit

Insert command: """)
                    found_profit = False
                    with open("Vehicles.txt", "r") as file:
                        lines = file.readlines()
                        for line in lines:
                            pre_profit = line.split(" | ")
                            searched_profit = pre_profit[7]
                            if d == "1" and int(searched_profit) == int(c):
                                found_profit = True
                                new_line = line.strip("\n")
                                print(new_line)
                            elif d == "2" and int(searched_profit) > int(c):
                                found_profit = True
                                new_line = line.strip("\n")
                                print(new_line)
                            elif d == "3" and int(searched_profit) < int(c):
                                found_profit = True
                                new_line = line.strip("\n")
                                print(new_line)
                        if d == "1" and found_profit == False:
                            print(f"No vehicles with a profit of {c} were found.\n")
                        elif d == "2" and found_profit == False:
                            print(f"No vehicles with more than {c} profit were found.\n")
                        elif d == "3" and found_profit == False:
                            print(f"No vehicles with less than {c} profit were found.\n")
                elif b == "9":
                    cycle_2 = False
                    cycle_3 = True
                    while cycle_3 == True:
                        c = input("""--- VEHICLE TYPE ---
1 - Car
2 - Van
    
Insert command: """)
                        if c == "1" or c == "2":
                            cycle_3 = False
                            found_type = False
                            with open("Vehicles.txt", "r") as file:
                                lines = file.readlines()
                                for line in lines:
                                    pre_type = line.split(" | ")
                                    searched_type = pre_type[8]
                                    if c == "1" and searched_type == "car":
                                        found_type = True
                                        new_line = line.strip("\n")
                                        print(new_line)
                                    elif c == "2" and searched_type == "van":
                                        found_type = True
                                        new_line = line.strip("\n")
                                        print(new_line)
                                if c == "1" and found_type == False:
                                    print("No cars were found.\n")
                                elif c == "2" and found_type == False:
                                    print("No vans were found.\n")
                        else:
                            print("Invalid command.\n")
                elif b == "10":
                    cycle_2 = False
                    cycle_3 = True
                    while cycle_3 == True:
                        c = input("""--- VEHICLE STATUS ---
1 - Active
2 - Inactive

Insert command: """)
                        if c == "1" or c == "2":
                            cycle_3 = False
                            found_status = False
                            with open("Vehicles.txt", "r") as file:
                                lines = file.readlines()
                                for line in lines:
                                    pre_status = line.split(" | ")
                                    searched_status = pre_status[13]
                                    if c == "1" and searched_status == "active":
                                        found_status = True
                                        new_line = line.strip("\n")
                                        print(new_line)
                                    elif c == "2" and searched_status == "inactive":
                                        found_status = True
                                        new_line = line.strip("\n")
                                        print(new_line)
                                if c == "1" and found_status == False:
                                    print("No active vehicles were found.\n")
                                elif c == "2" and found_status == False:
                                    print("No inactive vehicles were found.\n")
                        else:
                            print("Invalid command.\n")
                else:
                    print("Invalid Command.\n")
                
        else:
            print("Invalid command.\n")

def add():
    with open("Vehicles.txt", "r") as file:
        pre_id_counter = file.readlines()
        if pre_id_counter == []:
            id_counter = 1
        else:
            pre_id_counter_2 = pre_id_counter[-1]
            pre_id_counter_3 = pre_id_counter_2.split(" ")
            pre_id_counter_4 = pre_id_counter_3[0]
            id_counter = int(pre_id_counter_4) + 1
    a = input("Insert the vehicle's license: ")
    b = input("Insert the vehicle's manufacturer: ")
    c = input("Insert the vehicle's model: ")
    d = input("Insert the vehicle's driver: ")
    e = input("Insert the amount of kilometers travelled by the vehicle: ")
    f = input("Insert the amount of trips performed by the vehicle: ")
    g = input("Insert the amount of profit (in euros) generated by the vehicle: ")
    valid_type = False
    while valid_type == False:
        pre_h = input("""Is the vehicle a Car or a Van?
1 - Car
2 - Van

Insert number: """)
        if pre_h == "1":
            valid_type = True
            h = "car"
            i = 4
            j = 3
            k = 0.4
            l = 30
        elif pre_h == "2":
            valid_type = True
            h = "van"
            i = 6
            j = 4
            k = 0.7
            l = 25
        else:
            print("Invalid command.\n")
    m = "active"
    x = 2.5
    y = 2.5
    with open("Vehicles.txt", "a+") as file:
        file.write(f"{id_counter} | {a} | {b} | {c} | {d} | {e} | {f} | {g} | {h} | {i} | {j} | {k} | {l} | {m} | {x} | {y}\n")
    id_counter += 1
    print("VEHICLE SUCCESFULLY ADDED.")


def change_status():
    id_to_change = input("Insert the ID of the Vehicle which you want to deactivate/activate: ")
    new_lines = []
    with open("Vehicles.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            pre_items = line.split(" | ")
            searched_id = pre_items[0]
            status = pre_items[13]
            if id_to_change in searched_id:
                if "inactive" in status:
                    new_line = line.replace("inactive", "active")
                    new_lines.append(new_line)
                else:
                    new_line = line.replace("active", "inactive")
                    new_lines.append(new_line)
            else:
                new_lines.append(line)
    with open("Vehicles.txt", "w") as file:
            file.writelines(new_lines)
    print("VEHICLE STATUS SUCCESSFULLY CHANGED")


def request():
    valid_coordinates = False
    while valid_coordinates == False:
        user_x = float(input("Insert your x coordinate: "))
        user_y = float(input("Insert your y coordinate: "))
        if user_x <= 0 or user_x > 5 or user_y <= 0 or user_y > 5:
            print("Invalid coordinates.\n")
        else:
            destination_x = float(input("Insert your destination's x coordinate: "))
            destination_y = float(input("Insert your destination's y coordinate: "))
            if destination_x <= 0 or destination_x > 5 or destination_y <= 0 or destination_y > 5:
                print("Invalid coordinates.\n")
            else:
                valid_coordinates = True
                distance = math.hypot(destination_x - user_x, destination_y - user_y)
                rounded_distance = round(distance, 2)
                print(f"You are {rounded_distance} km away from your destination.\n")
                passengers = int(input("Insert number of passengers: "))
                print("--- AVAILABLE VEHICLES ---")
                with open("Vehicles.txt", "r") as file:
                    lines = file.readlines()
                    for line in lines:
                        new_line = line.split(" | ")
                        vehicle_type = new_line[8]
                        if passengers > 4 and vehicle_type == "car":
                            pass
                        else:
                            vehicle_x = new_line[14]
                            vehicle_y = new_line[15]
                            distance_to_user = math.hypot(user_x - float(vehicle_x), user_y - float(vehicle_y))
                            vehicle_speed = int(new_line[12])
                            time_to_user = distance_to_user / vehicle_speed
                            time_user_to_destination = distance / vehicle_speed
                            total_time = time_to_user + time_user_to_destination
                            total_time_mins = total_time * 60
                            rounded_total_time_mins = round(total_time_mins)
                            vehicle_id = new_line[0]
                            print(f"Vehicle {vehicle_id} will take you to your destination in {rounded_total_time_mins} minutes.")
                    confirm_request = input(f"\nInsert the ID of the vehicle you want to request (or 'c' to cancel): ")
                    found_id = False
                    if confirm_request == "c" or confirm_request == "C":
                        pass
                    else:
                        for line in lines:
                            pre_check_id = line.split(" | ")
                            check_id = pre_check_id[0]
                            if check_id == confirm_request:
                                found_id = True
                                print("VEHICLE SUCCESSFULLY REQUESTED")
                        if found_id == False:
                            print("No matching ID was found.")
