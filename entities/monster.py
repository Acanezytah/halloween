from persistence.db import get_connection


class Monster:

    def __init__(self, name, power, id=None):
        self.id = id
        self.name = name
        self.power = power

    @staticmethod
    def get_all():
        connection = get_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute('SELECT id, name, power FROM monster')
        monsters = cursor.fetchall()
        cursor.close()
        connection.close()
        return monsters

    @staticmethod
    def get_by_id(monster_id):
        connection = get_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute(
            'SELECT id, name, power FROM monster WHERE id = %s',
            (monster_id,)
        )
        monster = cursor.fetchone()
        cursor.close()
        connection.close()
        return monster

    def save(self):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute('INSERT INTO monster (name, power) VALUES (%s, %s)',
                       (self.name, self.power))
        connection.commit()
        cursor.close()
        connection.close()

    def update(self):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(
            'UPDATE monster SET name = %s, power = %s WHERE id = %s',
            (self.name, self.power, self.id)
        )
        connection.commit()
        cursor.close()
        connection.close()
