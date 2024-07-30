from models.__init__ import CONN, CURSOR


class Person:

    all = []

    def __init__(self, name, room=None, id=None):
        self.id = id
        self.name = name
        self.room = room
        self.chores = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError("Name must be a non-empty string")
        
    @property
    def room(self):
        return self._room

    @room.setter
    def room(self, room):
        if isinstance(room, str) and len(room):
            self._room = room
        else:
            raise ValueError("Room must be a non-empty string")

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
    def find_by_id(cls, id):
        sql = "SELECT * FROM person WHERE id = ?"
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        sql = "SELECT * FROM person WHERE name = ?"
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None

    def add_chore(self, chore):
        chore.person_id = self.id  # Set the person_id to the current person's id
        self.chores.append(chore)
        chore.save()

    def remove_chore(self, index):
        if 0 <= index < len(self.chores):
            self.chores.pop(index)
        else:
            print("Invalid index.")

    def update_chore(self, chore_index, task=None, status=None, priority=None):
        if 0 <= chore_index < len(self.chores):
            chore = self.chores[chore_index]
            if task:
                chore.task = task
            if status:
                chore.status = status
            if priority:
                chore.priority = priority
            print(f"Chore {chore.task} updated successfully.")
        else:
            print("Invalid chore index. Please try again.")

    def __str__(self):
        return f"{self.name} (Room: {self.room})"
