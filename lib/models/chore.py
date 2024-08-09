from models.__init__ import CONN, CURSOR

class Chore:

    def __init__(self, task, status, priority, person_id=0, id=None):
        self.id = id
        self.task = task
        self.status = status
        self.priority = priority
        self.person_id = person_id
        
    @property
    def task(self):
        return self._task

    @task.setter
    def task(self, task):
        if isinstance(task, str) and 2 <= len(task) <= 25:
            self._task = task
        else:
            raise ValueError("Task must be at least 2 characters and less than 25 characters long.")

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        status = status.strip().capitalize()
        if status in {"Pending", "Completed"}:
            self._status = status
        else:
            raise ValueError("Status must be 'Pending' or 'Completed'")

    @property
    def priority(self):
        return self._priority

    @priority.setter
    def priority(self, priority):
        priority = priority.strip().capitalize()
        if priority not in ["High", "Medium", "Low"]:
            raise ValueError("Priority must be one of: High, Medium, Low.")
        self._priority = priority

    @property
    def person_id(self):
        return self._person_id

    @person_id.setter
    def person_id(self, id):
        if isinstance(id, int):
            self._person_id = id
        else:
            raise ValueError("Person ID must be an integer")

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS chore (
                id INTEGER PRIMARY KEY,
                task TEXT,
                status TEXT,
                priority TEXT,
                person_id INTEGER,
                FOREIGN KEY (person_id) REFERENCES person(id)
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = "DROP TABLE IF EXISTS chore"
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        if self.id:
            self.update()
        else:
            sql = """
                INSERT INTO chore (task, status, priority, person_id)
                VALUES (?, ?, ?, ?)
            """
            CURSOR.execute(sql, (self.task, self.status, self.priority, self.person_id))
            CONN.commit()
            self.id = CURSOR.lastrowid

    @classmethod
    def create(cls, task, status, priority, person_id):
        chore = cls(task, status, priority, person_id)
        chore.save()
        return chore

    def update(self):
        sql = """
            UPDATE chore
            SET task = ?, status = ?, priority = ?, person_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.task, self.status, self.priority, self.person_id, self.id))
        CONN.commit()

    def delete(self):
        sql = "DELETE FROM chore WHERE id = ?"
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        chore = cls(row[1], row[2], row[3], row[4], row[0])
        return chore

    @classmethod
    def get_all(cls):
        sql = "SELECT * FROM chore"
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_task(cls, task):
        task = task.lower()
        sql = "SELECT * FROM chore WHERE LOWER(task) = ?"
        row = CURSOR.execute(sql, (task,)).fetchone()
        return cls.instance_from_db(row) if row else None