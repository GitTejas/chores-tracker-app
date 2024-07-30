from models.__init__ import CONN, CURSOR
from datetime import datetime

class Chore:

    all = []

    def __init__(self, task, due_date, status, priority, person_id=0, id=None):
        self.id = id
        self.task = task
        self.due_date = due_date
        self.status = status
        self.priority = priority
        self.person_id = person_id
        
        @property
        def task(self):
            return self._task

        @task.setter
        def task(self, task):
            if isinstance(task, str) and 1 <= len(task) <= 30:
                self._task = task
            else:
                raise ValueError("Task must be a string with 1 to 30 characters")
            
        @property
        def due_date(self):
            return self._due_date

        # @due_date.setter
        # def due_date(self, due_date):
        #     if isinstance(due_date, int):
        #         self._due_date = due_date
        #     else:
        #         raise ValueError("Due date must be an integer")
        
        @due_date.setter
        def due_date(self, due_date):
            try:
                datetime.strptime(due_date, "%Y/%m/%d")
                self._due_date = due_date
            except ValueError:
                raise ValueError("Due date must be in YYYY/MM/DD format")

        @property
        def status(self):
            return self._status

        @status.setter
        def status(self, status):
            if isinstance(status, str):
                self._status = status
            else:
                raise ValueError("Status must be a string")

        @property
        def priority(self):
            return self._priority

        @priority.setter
        def priority(self, priority):
            if isinstance(priority, str):
                self._priority = priority
            else:
                raise ValueError("Priority must be a string")

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
                due_date INTEGER,
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
                    INSERT INTO chore (task, due_date, status, priority, person_id)
                    VALUES (?, ?, ?, ?, ?)
                """
                CURSOR.execute(sql, (self.task, self.due_date, self.status, self.priority, self.person_id))
                CONN.commit()
                self.id = CURSOR.lastrowid
        
        @classmethod
        def create(cls, task, due_date, status, priority, person_id):
            chore = cls(task, due_date, status, priority, person_id)
            chore.save()
            return chore
        
        def update(self):
            sql = """
                UPDATE chore
                SET task = ?, due_date = ?, status = ?, priority = ?, person_id = ?
                WHERE id = >
            """
            CURSOR.execute(sql, (self.task, self.due_date, self.status, self.priority, self.person_id, self.id))
            CONN.commit()
            self.id = None

        def delete(self):
            sql = "DELETE FROM chore WHERE id = ?"
            CURSOR.execute(sql, (self.id,))
            CONN.commit()
            self.id = None
        
        @classmethod
        def instance_from_db(cls, row):
            chore = cls(row[1], row[2], row[3], row[4], row[5], row[0])
            return chore
        
        @classmethod
        def get_all(cls):
            sql = "SELECT * FROM chore"
            rows = CURSOR.execute(sql).fetchall()
            return [cls.instance_from_db(row) for row in rows]
        
        @classmethod
        def find_by_id(cls, id):
            sql = "SELECT * FROM chore WHERE id = ?"
            row = CURSOR.execute(sql, (id,)).fetchone
            return cls.instance_from_db(row) if row else None
        
        @classmethod
        def find_by_person_id(cls, person_id):
            sql = "SELECT * FROM chore WHERE person_id = ?"
            rows = CURSOR.execute(sql, (person_id)).fetchall()
            return [cls.instance_from_db(row) for row in rows]
        
        def ___repr__(self):
            return f"{self.task} - Due: {self.due_date} - Status: {self.status} - Priority: {self.priority}"