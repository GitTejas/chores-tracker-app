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
            if isinstance(task, str):
                self._task = task
            else:
                raise ValueError("Task must be a string")
            
        @property
        def due_date(self):
            return self._due_date
        
        @due_date.setter
        def due_date(self, due_date):
            try:
                datetime.strptime(due_date, "%Y/%m/%d")
                self._due_date = due_date
            except ValueError:
                raise ValueError("Due date must be in YYYY/MM/DD format")