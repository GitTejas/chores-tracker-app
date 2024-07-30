from models.__init__ import CONN, CURSOR

class Person:
    
    all = []

    def __init__(self, name, room, id):
        self.name = name
        self.room = room
        self.id = id

    