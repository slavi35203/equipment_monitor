import logic
import os
import time
import getpass

from logic import delete_user

current_user = None

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def login_screen():
    global current_user
    attempts = 0
    while attempts < 3:
        clear_screen()
        print("===== LOGIN =====")
        username = input("Username: ")
        password = input("Password: ")
        user = logic.authenticate_user(username, password)
        if user:
            current_user = user
            print(f"\nWelcome, {user['name']}!")
            time.sleep(1)
            return True
        else:
            print("Invalid credentials, try again.")
            attempts += 1
            time.sleep(1)
    print("Too many failed attempts. Exiting.")
    exit(1)

def display_menu():
    clear_screen()
    # print(f"Logged in as: {current_user['name']} ({current_user['role']})\n")
    if logic.is_admin(current_user):
        print("1. View all equipment")
        print("2. View equipment by type")
        print("3. Lookup protocols")
        print("4. Create new protocol")
        print("5. Mark protocol as returned")
        print("6. Manage users")
        print("7. Delete protocol")
        print("0. Logout")
    else:
        print("1. View my equipment")
        print("2. View my protocols")
        print("0. Logout")
    return input("\nChoice: ")

def view_all_equipment():
    equipment = logic.get_all_equipment()
    clear_screen()
    print("\n===== All Equipment ======")
    print(f"{'ID':<5} {'Brand':<15} {'Type':<20}")
    print("-" * 40)
    for e in equipment:
        print(f"{e['id']:<5} {e['Brand']:<15} {e['type']:<20}")
    input("\nPress Enter to continue...")

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


def view_all_users():
    users = logic.get_all_users()
    clear_screen()
    print("\n===== All Users =====")
    print(f"{'ID':<5} {'Name':<20} {'Username':<15} {'Role':<10} {'Active':<6}")
    print("-"*60)
    for u in users:
        active = 'Yes' if u['isActive'] else 'No'
        print(f"{u['id']:<5} {u['name']:<20} {u['username']:<15} {u['role']:<10} {active:<6}")
    input("\nPress Enter to continue...")


def add_new_user():
    clear_screen()
    print("\n===== Add New User =====")
    name = input("Full Name: ")
    username = input("Username: ")
    password = input("Password: ")
    role = input("Role (admin/employee): ").lower()
    if role not in ['admin', 'employee']:
        role = 'employee'
    depts = logic.get_all_departments()
    print("\nDepartments: ")
    for d in depts:
        print(f"{d['id']}: {d['name']}")
    try:
        dept_id = int(input("\nDepartment ID: "))
        if logic.add_user(name, username, password, role, dept_id):
            print("User added successfully!")
        else:
            print("Failed to add user (username may exist).")
    except ValueError:
        print("Invalid department ID.")
    time.sleep(1)

def edit_user():
    clear_screen()
    print("\n===== Edit User =====")
    print()

def deactivate_user():
    clear_screen()
    print("\n===== Deactivate User =====")
    try:
        user_id = int(input("User ID to deactivate: "))
        if logic.deactivate_user(user_id):
            print("User deactivated.")
        else:
            print("Failed to deactivate.")
    except ValueError:
        print("Invalid ID.")
    time.sleep(1)

def delete_protocol_ui():
    clear_screen()
    print("\n===== Delete Protocol =====")
    try:
        pid = int(input("Enter protocol ID to delete: "))
        confirm = input("Are you sure? This action cannot be undone (y/n): ")
        if confirm.lower() == 'y':
            if logic.delete_protocol(pid):
                print("Protocol deleted pernamently.")
            else:
                print("Failed to delete protocol.")
    except ValueError:
        print("Invalid ID.")
    time.sleep(1)

def user_management():
    while True:
        clear_screen()
        print("\n===== User Management =====")
        print("1. View all users")
        print("2. Add new user")
        print("3. Edit user")
        print("4. Deactivate user")
        print("5. Delete user")
        print("0. Back")
        choice = input("Choice: ")
        if choice == '1': view_all_users()
        elif choice == '2': add_new_user()
        elif choice == '3': edit_user()
        elif choice == '4': deactivate_user()
        elif choice == '5': delete_user_ui()
        elif choice == '0': break
        else: print("Invalid"); time.sleep(1)

def view_my_equipment():
    clear_screen()
    print("\n===== My Assigned Equipment =====")
    eqs = logic.get_user_equipment(current_user['id'])
    if not eqs:
        print("No equipment assigned.")
    else:
        print(f"{'ID':<5} {'Brand':<15} {'Type':<20} {'Date':<12}")
        print("-"*60)
        for e in eqs:
            print(f"{e['id']:<5} {e['Brand']:<15} {e['type']:<20} {e['assignedDate']:<12}")
    input("\nPress Enter to continue...")

def view_my_protocols():
    clear_screen()
    print("\n===== My Protocols =====")
    prots = logic.get_user_protocols(current_user['id'])
    if not prots:
        print("No protocols.")
    else:
        print(f"{'ID':<5} {'Type':<15} {'Date':<12} {'Returned':<8}")
        print("-"*50)
        for p in prots:
            ret = 'Yes' if p['isReturned'] else 'No'
            print(f"{p['id']:<5} {p['deviceType']:<15} {p['dateOfCreation']:<12} {ret:<8}")
    input("\nPress Enter to continue...")

def delete_user_ui():
    clear_screen()
    print("\n===== Delete User =====")
    try:
        uid = int(input("Enter user ID to delete:"))
        confirm = input("Are you sure? This action cannot be undone (y/n): ")

        if confirm.lower() == 'y':
            if logic.delete_protocol(uid):
                print("User deleted permanently.")
            else:
                print("Failed to delete user.")
    except ValueError:
        print("Invalid ID.")
    time.sleep(1)




def main_loop():
    global current_user
    if not login_screen():
        return
    print(f"Logged in as: {current_user['name']} ({current_user['role']})\n")
    while True:
        choice = display_menu()
        if choice == "0":
            print("Logging out...")
            current_user = None
            time.sleep(1)
            return

        if logic.is_admin(current_user):
            if choice == "1":
                view_all_equipment()
            elif choice == "2":
                view_equipment_by_type()
            elif choice == "3":
                lookup_protocol()
            elif choice == "4":
                create_new_protocol()
            elif choice == "5":
                mark_protocol_as_returned()
            elif choice == "6":
                user_management()
            elif choice == "7":
                delete_protocol_ui()
            else:
                print("Invalid choice.")
        else:
            if choice == "1":
                view_my_equipment()
            elif choice == "2":
                view_my_protocols()
            else:
                print("Invalid choice.")
        time.sleep(1)











