from typing import Dict, Optional


def create_customer(connection, customer_data: Dict) -> int:
    required_fields = ["firstname", "lastname", "email", "telephone", "password"]
    for field in required_fields:
        if field not in customer_data:
            raise ValueError(f"Missing required field: {field}")

    default_values = {
        "customer_group_id": 1,
        "store_id": 0,
        "language_id": 1,
        "custom_field": "",
        "newsletter": 0,
        "ip": "",
        "status": 1,
        "safe": 0,
        "token": "",
        "code": "",
    }

    customer_data = {**default_values, **customer_data}

    with connection.cursor() as cursor:
        sql = """INSERT INTO oc_customer (
            customer_group_id, store_id, language_id, firstname, lastname, 
            email, telephone, password, custom_field, newsletter, 
            ip, status, safe, token, code, date_added
        ) VALUES (
            %(customer_group_id)s, %(store_id)s, %(language_id)s, %(firstname)s, %(lastname)s, 
            %(email)s, %(telephone)s, %(password)s, %(custom_field)s, %(newsletter)s, 
            %(ip)s, %(status)s, %(safe)s, %(token)s, %(code)s, NOW()
        )"""
        cursor.execute(sql, customer_data)
        connection.commit()
        return cursor.lastrowid


def get_customer(connection, customer_id: int) -> Optional[Dict]:
    with connection.cursor() as cursor:
        sql = "SELECT * FROM oc_customer WHERE customer_id = %s"
        cursor.execute(sql, (customer_id,))
        return cursor.fetchone()


def update_customer(connection, customer_id: int, update_data: Dict) -> bool:
    if not update_data:
        return False

    set_clause = ", ".join([f"{key} = %({key})s" for key in update_data.keys()])
    sql = f"UPDATE oc_customer SET {set_clause} WHERE customer_id = %(customer_id)s"

    params = {**update_data, "customer_id": customer_id}

    with connection.cursor() as cursor:
        affected_rows = cursor.execute(sql, params)
        connection.commit()
        return affected_rows > 0


def delete_customer(connection, customer_id: int) -> bool:
    with connection.cursor() as cursor:
        sql = "DELETE FROM oc_customer WHERE customer_id = %s"
        affected_rows = cursor.execute(sql, (customer_id,))
        connection.commit()
        return affected_rows > 0
