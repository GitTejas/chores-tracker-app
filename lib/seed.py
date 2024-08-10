from models.person import Person
from models.chore import Chore

def seed():
    # Initialize database tables
    Person.drop_table()
    Chore.drop_table()
    Person.create_table()
    Chore.create_table()

    # Create people and store their IDs
    bella = Person.create(name="Bella", room="Kitchen")
    # print(f"Created Bella with ID: {bella.id}")
    
    keiji = Person.create(name="Keiji", room="Living Room")
    # print(f"Created Keiji with ID: {keiji.id}")
    
    serenity = Person.create(name="Serenity", room="Garden")
    # print(f"Created Serenity with ID: {serenity.id}")
    
    agheel = Person.create(name="Agheel", room="Garage")
    # print(f"Created Agheel with ID: {agheel.id}")

    # Create chores and assign them to the appropriate person
    Chore.create(task="Clean the kitchen", status="Pending", priority="High", person_id=bella.id)
    Chore.create(task="Do the Laundry", status="Pending", priority="Medium", person_id=bella.id)
    Chore.create(task="Vacuum the living room", status="Completed", priority="Low", person_id=keiji.id)
    Chore.create(task="Take out the trash", status="Pending", priority="High", person_id=keiji.id)
    Chore.create(task="Water the plants", status="Pending", priority="High", person_id=serenity.id)
    Chore.create(task="Mow the Lawn", status="Completed", priority="Low", person_id=serenity.id)
    Chore.create(task="Organize tools", status="Pending", priority="Medium", person_id=agheel.id)
    Chore.create(task="Clean the car", status="Pending", priority="High", person_id=agheel.id)

    print("Seeding Successful!")

# Call the seed function
seed()