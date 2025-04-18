import sqlite3

def update_schema():
    conn = sqlite3.connect('monitoringtool.db')
    cursor = conn.cursor()

    cursor.execute("PRAGMA table_info(Users)")
    columns = [column[1] for column in cursor.fetchall()]

    if 'username' not in columns:
        cursor.execute("ALTER TABLE Users ADD COLUMN username TEXT")
        print("Added username column to Users table")

    if 'password' not in columns:
        cursor.execute("ALTER TABLE Users ADD COLUMN password TEXT")
        print("Added password column to Users table")

    if 'role' not in columns:
        cursor.execute("ALTER TABLE Users ADD COLUMN role TEXT DEFAULT 'employee'")
        print("Added role column to Users table")

    cursor.execute("""
        CREATE UNIQUE INDEX IF NOT EXISTS idx_users_username
        ON Users(username)
    """)
    print("Ensure UNIQUE index on Users.username")

    conn.commit()
    conn.close()

    print("Schema update completed successfully!")

if __name__ == "__main__":
    update_schema()