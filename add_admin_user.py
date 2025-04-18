import sqlite3
import hashlib


def add_admin_user():
    conn = sqlite3.connect('monitoringtool.db')
    cursor = conn.cursor()


    cursor.execute("SELECT id FROM Users WHERE username = 'admin'")
    if not cursor.fetchone():
        pwd = "admin123"
        hashed = hashlib.sha256(pwd.encode('utf-8')).hexdigest()

        cursor.execute("""
            INSERT INTO Users (name, username, password, role, isActive, departmentId)
            VALUES (?, ?, ?, ?, ?, ?)
            """, ("Administrator", "admin", hashed, "admin", 1, 1))
        print("Admin user created successfully!")
    else:
        print("Admin user already exists.")

    conn.commit()
    conn.close()

if __name__ == "__main__":
    add_admin_user()