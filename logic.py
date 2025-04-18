from db import get_connection, execute_query, execute_update, get_single_record

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
        (userId, deviceType, phoneId, stationaryId, equipmentId, simId, deviceOfCreation, createdBy, isReturned)
        VALUES (?, ?, ?, ?, ?, ?, date('now'), ?, 0)
    """
    params = (user_id, device_type, phone_id, stationary_id, equipment_id, sim_id, created_by)

    return execute_update(query, params)

def mark_protocol_returned(protocol_id, returned_by):
    query = """
        UPDATE Protocols
        SET isReturned = 1, returnedBy = ?
        WHERE id = ?
    """
    return execute_update(query, (returned_by, protocol_id))


