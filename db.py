import sqlite3


def get_connection():
    return sqlite3.connect("monitoringtool.db")

def get_user_by_username(username):
    conn = get_connection()
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("SELECT * FROM Users WHERE username = ?", (username,))
    user = cur.fetchone()
    conn.close()
    return user

def execute_query(query, params = None):
    conn = get_connection()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    if params:
        cursor.execute(query, params)
    else:
        cursor.execute(query)

    results = cursor.fetchall()
    conn.commit()
    conn.close()
    return results

def execute_update(query, params = None):
    conn = get_connection()
    cursor = conn.cursor()

    if params:
        cursor.execute(query, params)
    else:
        cursor.execute(query)

    row_count = cursor.rowcount
    conn.commit()
    conn.close()
    return row_count

def get_single_record(query, params = None):
    conn = get_connection()
    cursor = conn.cursor()

    if params:
        cursor.execute(query,params)
    else:
        cursor.execute(query)

    result = cursor.fetchone()
    conn.close()
    return result

