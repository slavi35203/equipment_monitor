import sqlite3

conn = sqlite3.connect('monitoringtool.db')
cursor = conn.cursor()

# cursor.execute("""
#     DROP TABLE Users
# """)
# conn.commit()

# cursor.execute("""
#     DROP TABLE Phones
# """)
# conn.commit()

# cursor.execute("""
#     DROP TABLE Stationary
# """)
# conn.commit()

# cursor.execute("""
#     DROP TABLE Equipment
# """)
# conn.commit()

# cursor.execute("""
#     DROP TABLE EquipmentTypes
# """)
# conn.commit()

# cursor.execute("""
#     DROP TABLE SIM
# """)
# conn.commit()

# cursor.execute("""
#     DROP TABLE Protocols
# """)
# conn.commit()

# cursor.execute("""
#     DROP TABLE Departments
# """)
# conn.commit()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Phones(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	purchasedDate DATE,
	IMEI TEXT,
	Brand TEXT,
	Model TEXT
)
""")
conn.commit()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name = 'Phones'")
result1 = cursor.fetchone()

if result1:
    print("Table Phones created successfully!")
else:
    raise Exception("Error creating the table Phones")


cursor.execute("""
    CREATE TABLE IF NOT EXISTS EquipmentTypes(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
    type VARCHAR(255)
)
""")
conn.commit()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name = 'EquipmentTypes'")
result4 = cursor.fetchone()

if result4:
    print("Table EquipmentTypes created successfully!")
else:
    raise Exception("Error creating the table EquipmentTypes")


cursor.execute("""
    CREATE TABLE IF NOT EXISTS Equipment(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	startDate DATE,
	typeId INTEGER,
	Brand VARCHAR(255),
	endDate DATE,
	ip TEXT,
    FOREIGN KEY(typeId) REFERENCES EquipmentTypes(id)
)
""")
conn.commit()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name = 'Equipment'")
result3 = cursor.fetchone()

if result3:
    print("Table Equipment created successfully!")
else:
    raise Exception("Error creating the table Equipment")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Stationary (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    purchaseDate DATE,
	inUse BOOLEAN
)
""")
conn.commit()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name = 'Stationary'")
result2 = cursor.fetchone()

if result2:
    print("Table Stationary created successfully!")
else:
    raise Exception("Error creating the table Stationary")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Departments(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
    )
""")
conn.commit()

cursor.execute("SELECT name FROM sqlite_master WHERE type = 'table' AND name = 'Departments'")
result7 = cursor.fetchone

if result7:
    print("Table Departments is created successfully!")
else:
    raise Exception("Error creating table Departments!")


cursor.execute("""
CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255) NOT NULL,
    departmentId INTEGER,
    isActive BOOLEAN,
    typeId INTEGER,
    notes TEXT,
    sex CHAR,
    FOREIGN KEY(departmentId) REFERENCES Departments(id)
)
""")
conn.commit()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name = 'Users'")
result0 = cursor.fetchone()

if result0:
    print("Table Users created successfully!")
else:
    raise Exception("Error creating the table Users")



cursor.execute("""
    CREATE TABLE IF NOT EXISTS SIM(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	activationDate DATE,
	limitMinutes INT,
	simNotes TEXT,
	phoneNumber CHAR(10),
	pin CHAR(4),
	puk CHAR(10),
	provider TEXT
)
""")
conn.commit()

cursor.execute("SELECT name FROM sqlite_master WHERE type ='table' AND name = 'SIM'")
result5 = cursor.fetchone

if result5:
    print("Table SIM created successfully!")
else:
    raise Exception("Error creating the table SIM")


cursor.execute("""
    CREATE TABLE IF NOT EXISTS Protocols(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    userId INTEGER,
    deviceType TEXT,
    phoneId INTEGER,
    stationaryId INTEGER,
    equipmentId INTEGER,
    simId INTEGER,
    dateOfCreation DATE,
    createdBy TEXT,
    modifiedBy TEXT,
    isRetured BOOLEAN,
    returnedBy TEXT,
    FOREIGN KEY(userId) REFERENCES Users(id),
    FOREIGN KEY(phoneId) REFERENCES Phones(id),
    FOREIGN KEY(stationaryId) REFERENCES Stationary(id),
    FOREIGN KEY(equipmentId) REFERENCES Equipment(id),
    FOREIGN KEY(simId) REFERENCES SIM(id)
    )
""")
conn.commit()

cursor.execute("SELECT name FROM sqlite_master WHERE type = 'table'AND name = 'Protocols'")
result6 = cursor.fetchone

if result6:
    print("Table Protocols created successfully!")
else:
    raise Exception("Error creating table Protocols!")
