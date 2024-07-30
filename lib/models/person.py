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
        if isinstance(name, str) and 2 <= len(name) <= 15:
            self._name = name
        else:
            raise ValueError("Name must be a string with 2 to 15 characters")
        
    @property
    def room(self):
        return self._room 
    
    @room.setter
    def room(self, room):
        if isinstance(room, str) and 2 <= len(room) <= 20:
            self._room = room
        else:
            raise ValueError("Room must be a string with 2 to 20 characters")
    
