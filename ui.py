import logic

def display_menu():
    print("\n==========================")
    print("1. Login")
    print("2. View all equipment")
    print("3. View equipment by type")
    print("4. Look up protocol")
    print("5. Create new protocol")
    print("6. Mark protocol as returned")
    print("0. Exit")
    return input("Enter your choice: ")

def view_all_equipment():
    equpment = logic.get_all_equipment()
    print("\n===== All Equipment ======")
    print(f"{'ID':<5} {'Brand':<15} {'Type':<20}")
    print("-" * 40)

    for item in equpment:
        print(f"{item[0]:<5} {item[1]:<15} {item[2]:<20}")

def view_equipment_by_type():
    types = logic.get_equipment_types()

    print("\n====== Equipment Types =====")
    for t in types:
        print(f"{t[0]}: {t[1]}")

    type_id = input("\nEnter type ID to filter (or 0 to cancel): ")
    if type_id == '0':
        return

    try:
        type_id = int(type_id)
        equipment = logic.get_equipment_by_type(type_id)

        print(f"\n===== Equipment of Type {type_id} =====")
        print(f"{'ID':<5} {'Brand':<15} {'IP':<15} {'Start Date':<12}")
        print("-" * 47)

        for item in equipment:
            print(f"{item[0]:<5} {item[1]:<15} {item[2]:<15} {item[3]:<12}")

    except ValueError:
        print("Invalid input. Please enter a number.")


def lookup_protocol():
    protocol_id = input("Enter protocol ID: ")

    try:
        protocol_id = int(protocol_id)
        protocol = logic.get_protocol_by_id(protocol_id)

        if protocol:
            print("\n===== Protocol Details =====")
            print(f"Protocol ID: {protocol[0]}")
            print(f"User ID: {protocol[1]}")
            print(f"Device Type: {protocol[2]}")

            user = logic.get_user_by_id(protocol[1])
            if user:
                print(f"Assigned to: {user[1]}")

            print(f"Created on: {protocol[7]}")
            print(f"Returned: {'Yes' if protocol[10] else 'No'}")

        else:
            print("Protocol not found.")

    except ValueError:
        print("Invalid input. Please enter a number.")


def create_new_protocol():
    user_id = input("Enter user ID: ")
    device_type = input("Enter device type (Phone, Equipment, Stationary, SIM): ")

    item_id = None
    if device_type.lower() == "phone":
        phone_id = input("Enter phone ID: ")
        item_id = int(phone_id) if phone_id.isdigit() else None
        if logic.create_protocol(user_id, device_type, phone_id=item_id):
            print("Protocol created successfully!")
    elif device_type.lower() == "equipment":
        equipment_id = input("Enter equipment ID: ")
        item_id = int(equipment_id) if equipment_id.isdigit() else None
        if logic.create_protocol(user_id, device_type, equipment_id=item_id):
            print("Protocol created successfully!")

    else:
        print("Invalid device type!")


def mark_protocol_as_returned():
    protocol_id = input("Enter protocol ID: ")
    returned_by = input("Returned by (name): ")

    if logic.mark_protocol_returned(protocol_id, returned_by):
        print("Protocol marked as returned successfully!")
    else:
        print("Failed to update protocol. Please check the ID.")

def main_loop():
    while True:
        choice = display_menu()

        if choice == '1':
            print("Login functionality not implemented yet.")
        elif choice == '2':
            view_all_equipment()
        elif choice == '3':
            view_equipment_by_type()
        elif choice == '4':
            lookup_protocol()
        elif choice == '5':
            create_new_protocol()
        elif choice == '6':
            mark_protocol_as_returned()
        elif choice == '0':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")












