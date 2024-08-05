from models.person import Person
from models.chore import Chore

def seed():
    # Initialize database tables
    Person.drop_table()
    Chore.drop_table()
    Person.create_table()
    Chore.create_table()

    # Create people
    Person.create(name="Bella", room="Kitchen")
    Person.create(name="Keiji", room="Living Room")
    Person.create(name="Serenity", room="Garden")
    Person.create(name="Agheel", room="Garage")

    # Fetch all people from the database
    all_people = Person.get_all()

    # Add chores to each person
    for person in all_people:
        if person.name == "Bella":
            chore1 = Chore.create(task="Clean the kitchen", status="Pending", priority="High", person_id=person.id)
            chore2 = Chore.create(task="Do the Laundry", status="Pending", priority="Medium", person_id=person.id)
            person.add_chore(chore1)
            person.add_chore(chore2)
        elif person.name == "Keiji":
            chore3 = Chore.create(task="Vacuum the living room", status="Completed", priority="Low", person_id=person.id)
            chore4 = Chore.create(task="Take out the trash", status="Pending", priority="High", person_id=person.id)
            person.add_chore(chore3)
            person.add_chore(chore4)
        elif person.name == "Serenity":
            chore5 = Chore.create(task="Water the plants", status="Pending", priority="High", person_id=person.id)
            chore6 = Chore.create(task="Mow the Lawn", status="Completed", priority="Low", person_id=person.id)
            person.add_chore(chore5)
            person.add_chore(chore6)
        elif person.name == "Agheel":
            chore7 = Chore.create(task="Organize tools", status="Pending", priority="Medium", person_id=person.id)
            chore8 = Chore.create(task="Clean the car", status="Pending", priority="High", person_id=person.id)
            person.add_chore(chore7)
            person.add_chore(chore8)

    return all_people

people = seed()
print("Seeding Successful!")
