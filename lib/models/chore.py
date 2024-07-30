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
        
        @due_date.setter
        def due_date(self, due_date):
            try:
                datetime.strptime(due_date, "%Y/%m/%d")
                self._due_date = due_date
            except ValueError:
                raise ValueError("Due date must be in YYYY/MM/DD format")
            
        # @due_date.setter
        # def due_date(self, due_date):
        #     if isinstance(due_date, int):
        #         self._due_date = due_date
        #     else:
        #         raise ValueError("Due date must be an integer")

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
