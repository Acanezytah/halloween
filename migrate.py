from persistence.db import get_connection

connection = get_connection()
cursor = connection.cursor()

try:
    cursor.execute(
        'ALTER TABLE monster ADD COLUMN image_url VARCHAR(2048) NULL'
    )
    connection.commit()
finally:
    cursor.close()
    connection.close()