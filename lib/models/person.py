from models.__init__ import CONN, CURSOR

class Person:

    def __init__(self, name, room=None, id=None):
        self.id = id
        self.name = name
        self.room = room

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 < len(name) < 15:
            self._name = name
        else:
            raise ValueError("Name must be greater than 1 character and less than 15 characters. Please enter a valid name.")
        
    @property
    def room(self):
        return self._room

    @room.setter
    def room(self, room):
        if isinstance(room, str) and room.strip():
            self._room = room
        else:
            raise ValueError("Room cannot be empty. Please enter a valid room.")

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS person (
                id INTEGER PRIMARY KEY,
                name TEXT,
                room TEXT
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = "DROP TABLE IF EXISTS person"
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        if self.id:
            self.update()
        else:
            sql = "INSERT INTO person (name, room) VALUES (?, ?)"
            CURSOR.execute(sql, (self.name, self.room))
            CONN.commit()
            self.id = CURSOR.lastrowid

    @classmethod
    def create(cls, name, room=None):
        person = cls(name, room)
        person.save()
        return person

    def update(self):
        sql = "UPDATE person SET name = ?, room = ? WHERE id = ?"
        CURSOR.execute(sql, (self.name, self.room, self.id))
        CONN.commit()

    def delete(self):
        sql = "DELETE FROM person WHERE id = ?"
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        person = cls(row[1], row[2], row[0])
        return person

    @classmethod
    def get_all(cls):
        sql = "SELECT * FROM person"
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_name(cls, name):
        name = name.lower()
        sql = "SELECT * FROM person WHERE LOWER(name) = ?"
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_id(cls, id):
        sql = "SELECT * FROM person WHERE id = ?"
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    def chore(self):
       from models.chore import Chore
       sql = "SELECT * FROM chore WHERE person_id = ?"
       CURSOR.execute(sql, (self.id,))
       rows = CURSOR.fetchall()
       return [Chore.instance_from_db(row) for row in rows]