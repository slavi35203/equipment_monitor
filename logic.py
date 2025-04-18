from db import get_connection, execute_query, execute_update, get_single_record, get_user_by_username
import hashlib


def get_all_equipment():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT Equipment.id, Equipment.Brand, EquipmentTypes.type
        FROM Equipment
        JOIN EquipmentTypes ON Equipment.typeId = EquipmentTypes.id
    """)
    rows = cursor.fetchall()
    conn.close()
    return rows

def get_equipment_by_type(type_id):
    query = """
        SELECT Equipment.id, Equipment.Brand, Equipment.id, Equipment.startDate
        FROM Equipment
        WHERE Equipment.typeId = ?
    """
    return execute_query(query, (type_id,))

def get_equipment_types():
    query = "SELECT id, type FROM EquipmentTypes"
    return execute_query(query)

def get_all_phones():
    query = "SELECT id, IMEI, Brand, Model FROM Phones"
    return execute_query(query)

def get_user_by_id(user_id):
    query = "SELECT * FROM Users WHERE id = ?"
    return get_single_record(query, (user_id,))

def get_protocol_by_id(protocol_id):
    query = "SELECT * FROM Protocols WHERE id = ?"
    return get_single_record(query, (protocol_id,))

def get_user_protocols(user_id):
    query = """
        SELECT p.id, p.deviceType, p.dateOfCreation, p.isReturned
        FROM Protocols p
        WHERE p.userId = ?
    """
    return execute_query(query, (user_id,))

def create_protocol(user_id, device_type, phone_id = None, stationary_id = None, equipment_id = None, sim_id = None, created_by = "System"):
    query = """
        INSERT INTO Protocols
        (userId, deviceType, phoneId, stationaryId, equipmentId, simId, dateOfCreation, createdBy, isRetured)
        VALUES (?, ?, ?, ?, ?, ?, date('now'), ?, 0)
    """
    params = (user_id, device_type, phone_id, stationary_id, equipment_id, sim_id, created_by)

    return execute_update(query, params)

def mark_protocol_returned(protocol_id, returned_by):
    query = """
        UPDATE Protocols
        SET isRetured = 1, returnedBy = ?
        WHERE id = ?
    """
    return execute_update(query, (returned_by, protocol_id))


def authenticate_user(username: str, password: str) -> dict:
    """Checks if username + pass.
        Returns dict with user or None."""
    user = get_user_by_username(username)
    if not user or user["isActive"] != 1:
        return None

    hashed_input = hashlib.sha256(password.encode("utf-8")).hexdigest()
    if user["password"] != hashed_input:
        return None

    user = dict(user)

    return {
        "id": user["id"],
        "name": user["name"],
        "username": user["username"],
        "role": user.get("role", "employee"),
        "department_id": user["departmentId"],
        "is_active": user["isActive"]
        }

def is_admin(user: dict) -> bool:
    """Returns True if a user is admin"""
    return bool(user and user.get("role") == "admin")

def get_all_users():
    return execute_query("SELECT * FROM Users")

def get_all_departments():
    return execute_query("SELECT * FROM Departments")

def add_user(name, username, password, role, department_id):
    if get_user_by_username(username):
        return False

    pwd_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()

    query = """
        INSERT INTO Users (name, username, password, role, departmentId, isActive)
        VALUES (?, ?, ?, ?, ?, 1)"""
    return execute_update(query, (name, username, pwd_hash, role, department_id))

def deactivate_user(user_id):
    return execute_update("UPDATE Users SET isActive = 0 WHERE id = ?", (user_id,)) > 0


def get_user_equipment(user_id):
    query = """
        SELECT e.id, e.Brand, et.type, p.dateOfCreation AS assignedDate
        FROM Equipment e
        JOIN EquipmentTypes et ON e.typeId = et.id
        JOIN Protocols p ON p.equipmentId = e.id
        WHERE p.userId = ? AND p.isRetured = 0
    """
    return execute_query(query, (user_id,))













