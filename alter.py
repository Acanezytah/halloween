from persistence.db import get_connection


def main():
    connection = get_connection()
    cursor = None

    try:
        cursor = connection.cursor()
        cursor.execute(
            'ALTER TABLE monster MODIFY COLUMN power TEXT NOT NULL'
        )
        connection.commit()
        print('La columna monster.power ahora es TEXT NOT NULL.')
    finally:
        if cursor is not None:
            cursor.close()
        connection.close()


if __name__ == '__main__':
    main()