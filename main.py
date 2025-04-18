import update_schema
from ui import main_loop
from add_admin_user import add_admin_user


def main():
    print("Welcome to Equipment Management System")
    print("-------------------------------------")
    update_schema.update_schema()
    add_admin_user()

    main_loop()

if __name__ == "__main__":
    main()