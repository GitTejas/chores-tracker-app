from models.person import Person
from models.chore import Chore

def seed_database():
    Person.drop_table()
    Chore.drop_table()
    Person.create_table()
    Chore.create_table()

    person1 = Person.create(name="Bella", room="Kitchen")
    person2 = Person.create(name="Keiji", room="Living Room")
    person3 = Person.create(name="Serenity", room="Garden")
    person4 = Person.create(name="Agheel", room="Garage")

    # Add chores to person1
    chore1 = Chore.create(task="Clean the kitchen", due_date="2024/07/31", status="Pending", priority="High", person_id=person1.id)
    chore2 = Chore.create(task="Do the Laundry", due_date="2024/07/30", status="Pending", priority="Medium", person_id=person2.id)
    person1.add_chore(chore1)
    person1.add_chore(chore2)

    # Add chores to person2
    chore3 = Chore.create(task="Vacuum the living room", due_date="2024/07/29", status="Completed", priority="Low", person_id=person2.id)
    chore4 = Chore.create(task="Take out the trash", due_date="2024/07/28", status="Pending", priority="Immediate", person_id=person2.id)
    person2.add_chore(chore3)
    person2.add_chore(chore4)

    # Add chores to person3
    chore5 = Chore.create(task="Water the plants", due_date="2024/07/31", status="Pending", priority="High", person_id=person3.id)
    chore6 = Chore.create(task="Mow the Lawn", due_date="2024/07/28", status="Completed", priority="Low", person_id=person3.id)
    person3.add_chore(chore5)
    person3.add_chore(chore6)

    # Add chores to person4
    chore7 = Chore.create(task="Organize tools", due_date="2024/08/01", status="Pending", priority="Medium", person_id=person4.id)
    chore8 = Chore.create(task="Clean the car", due_date="2024/08/02", status="Pending", priority="High", person_id=person4.id)
    person4.add_chore(chore7)
    person4.add_chore(chore8)

    return [person1, person2, person3, person4]

people = seed_database()
print("Seeding Successful!")
