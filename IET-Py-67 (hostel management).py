rooms ={
    101: 'Ayesha',
    102: 'Tayyaba',
    103: None,
    104: None
}

# Showing menu 
def show_menu():
    print("\n---------Hostel Room Mnagement--------")
    print("1. Assign Rooms")
    print("2.Vacate Room")
    print("3.View all the Rooms")
    print("4. Search Rooms/Students")
    print("5.Show Vacant Rooms")
    print("6.Exit")
# Assign rooms
def assign_room():
    room = int(input("Enter room number to assign: "))
    if room not in rooms:
        print("Room does not exist!")
    elif rooms[room] is not None:
        print(f"Room {room} is already occupied by {rooms[room]}.")
    else:
        name = input("Enter student name: ")
        rooms[room] = name
        print(f"{name} has been assigned to room {room}.")
#Vacate rooms
def vacate_room():
    room = int(input("Enter room number to vacate: "))
    if room not in rooms:
        print("Room does not exist!")
    elif rooms[room] is None:
        print(f"Room {room} is already vacant.")
    else:
        print(f"{rooms[room]} has vacated room {room}.")
        rooms[room] = None
#   View Rooms
def view_rooms():
    print("\nRoom Status:")
    for room, name in rooms.items():
        status = name if name else "Vacant"
        print(f"Room {room}: {status}")
#Search Room students
def search_room_student():
    choice = input("Search by (1) Room or (2) Student? ")
    if choice == '1':
        room = int(input("Enter room number: "))
        if room in rooms:
            print(f"Room {room} is {'Vacant' if rooms[room] is None else rooms[room]}")
        else:
            print("Room does not exist!")
    elif choice == '2':
        student = input("Enter student name: ")
        found = False
        for room, name in rooms.items():
            if name == student:
                print(f"{student} is in room {room}")
                found = True
        if not found:
            print(f"{student} is not assigned to any room.")
    else:
        print("Invalid choice!")
#Shor vacant room
def show_vacant_rooms():
    vacant = [room for room, name in rooms.items() if name is None]
    print("Vacant Rooms:", vacant if vacant else "No vacant rooms")
#Main Program
while True:
    show_menu()
    option = input("Choose an option: ")
    if option == '1':
        assign_room()
    elif option == '2':
        vacate_room()
    elif option == '3':
        view_rooms()
    elif option == '4':
        search_room_student()
    elif option == '5':
        show_vacant_rooms()
    elif option == '6':
        print("Exiting program...")
        break
    else:
        print("Invalid option, try again!")
