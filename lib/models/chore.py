from models.__init__ import __init__


class Chore:

    all = []

    def __init__(self, task, due_date, status, priority, person_id, id):
        self.task = task
        self.status = status
        self.due_date = due_date
        self.priority = priority
        self.person_id = person_id
        self.id = id
        