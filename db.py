import sqlite3


def get_connection():
    return sqlite3.connect("monitoringtool.db")

def execute_query(query, params = None):
    conn = get_connection()
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

