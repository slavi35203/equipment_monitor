import sqlite3

conn = sqlite3.connect('monitoringtool.db')
cursor = conn.cursor()
cursor.execute("UPDATE Users SET isActive = 1 WHERE username = 'admin'")
conn.commit()
conn.close()
print("Admin reactivated.")