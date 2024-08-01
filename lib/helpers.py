from models.chore import Chore
from models.person import Person

# def get_all_people():
#     return Person.get_all()

def list_people(people):
    people = Person.get_all()
    for index, person in enumerate(people):
        print(f"{index + 1}. {person}")

def add_person(people):
    while True:
        name = input("Enter the person's name: ").strip()
        if not name:
            print("Name cannot be empty. Please enter a valid name.")
            continue
        if name.isdigit():
            print("Name cannot be a digit. Please enter a valid name.")
            continue
        if len(name) <= 1 or len(name) >= 15:
            print("Name must be greater than 1 characters and less than 15 characters. Please enter a valid name.")
            continue  
        room = input("Enter the person's room: ").strip()
        if not room:
            print("Room cannot be empty. Please enter a valid room.")
            continue
        if room.isdigit():
            print("Room cannot be all digits. Please enter a valid room.")
            continue
        new_person = Person(name=name, room=room)
        new_person.save()  # Saved to the database
        people.append(new_person)
        print(f"Person '{name}' added.")
        break

def delete_person(people):
    list_people(people)
    try:
        index = int(input("Enter the number of the person to delete: ")) - 1
        if 0 <= index < len(people):
            deleted_person = people.pop(index)
            deleted_person.delete()  # Deleted from the database
            print(f"Person '{deleted_person.name}' deleted.")
        else:
            print("Invalid selection.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def update_person(people):
    list_people(people)
    try:
        index = int(input("Enter the number of the person to update: ")) - 1
        if 0 <= index < len(people):
            person = people[index]
            # Update name with validation
            while True:
                new_name = input(f"Enter new name for {person.name} (leave blank to keep current): ").strip()
                if new_name == "":
                    new_name = person.name  # Keep the current name if left blank
                    break
                if new_name.isdigit():
                    print("Name cannot be all digits. Please enter a valid name.")
                    continue
                if len(new_name) <= 2 or len(new_name) >= 20:
                    print("Name must be greater than 2 characters and less than 20 characters.")
                    continue
                person.name = new_name
                break
            # Update room with validation
            while True:
                new_room = input(f"Enter new room for {person.room} (leave blank to keep current): ").strip()
                if new_room == "":
                    new_room = person.room  # Keep the current room if left blank
                    break
                if new_room.isdigit():
                    print("Room cannot be all digits. Please enter a valid room.")
                    continue
                person.room = new_room
                break
            person.save()  # Updated in the database
            print(f"Person '{person.name}' updated.")
        else:
            print("Invalid selection.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def list_chores(people):
    print("Chores List:")
    for person in people:
        print("---------------------------------------------------------------------")
        print(f"{person.name} (Room: {person.room})")
        for index, chore in enumerate(person.chores):
            print(f"  {index + 1}. Task: {chore.task} | Status: {chore.status} | Priority: {chore.priority}")
        print("---------------------------------------------------------------------")
        
def add_chore(people):
    list_people(people)
    try:
        index = int(input("Enter the number of the person to add a chore for: ")) - 1
        if 0 <= index < len(people):
            person = people[index]
            task = input("Enter the task: ")
            while True:
                status = input("Enter the status (Pending or Completed): ")
                if status in ["Pending", "Completed"]:
                    break
                else:
                    print("Invalid status. Please enter 'Pending', or 'Completed'.")
            while True:
                priority = input("Enter the priority (High, Medium, Low): ")
                if priority in ["High", "Medium", "Low"]:
                    break
                else:
                    print("Invalid priority. Please enter 'High', 'Medium', or 'Low'.")
            # Create and add the chore
            chore = Chore(task=task, status=status, priority=priority, person_id=person.id)
            person.add_chore(chore)
            print(f"Chore '{task}' added for {person.name}.")
        else:
            print("Invalid selection.")
    except ValueError as ve:
        print(f"Invalid input: Please enter a valid number.")


def delete_chore(people):
    list_people(people)
    try:
        person_index = int(input("Enter the number of the person to delete a chore for: ")) - 1
        if 0 <= person_index < len(people):
            person = people[person_index]
            for index, chore in enumerate(person.chores):
                print(f"  {index + 1}. {chore}")
            chore_index = int(input("Enter the number of the chore to delete: ")) - 1
            if 0 <= chore_index < len(person.chores):
                deleted_chore = person.chores.pop(chore_index)
                deleted_chore.delete()  # Deleted from the database
                print(f"Chore '{deleted_chore.task}' deleted.")
            else:
                print("Invalid selection.")
        else:
            print("Invalid selection.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def update_chore(people):
    list_people(people)
    try:
        person_index = int(input("Enter the number of the person to update a chore for: ")) - 1
        if 0 <= person_index < len(people):
            person = people[person_index]
            for index, chore in enumerate(person.chores):
                print(f"  {index + 1}. {chore}")
            chore_index = int(input("Enter the number of the chore to update: ")) - 1
            if 0 <= chore_index < len(person.chores):
                chore = person.chores[chore_index]
                # Ask for new task
                new_task = input(f"Enter new task for '{chore.task}' (leave blank to keep current): ")
                if new_task:
                    chore.task = new_task
                # Ask for new status
                while True:
                    new_status = input(f"Enter new status for '{chore.status}' (leave blank to keep current): ")
                    if new_status in ["Pending", "Completed"]:
                        if new_status:
                            chore.status = new_status
                        break
                    else:
                        print("Invalid priority. Please enter 'Pending', or 'Completed'.")
                # Ask for new priority with validation loop
                while True:
                    new_priority = input(f"Enter new priority for '{chore.priority}' (leave blank to keep current): ")
                    if new_priority in ["High", "Medium", "Low", ""]:
                        if new_priority:
                            chore.priority = new_priority
                        break
                    else:
                        print("Invalid priority. Please enter 'High', 'Medium', or 'Low'.")
                chore.save()  # Updated in the database
                print(f"Chore '{chore.task}' updated.")
            else:
                print("Invalid selection.")
        else:
            print("Invalid selection.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def find_person_by_name(people):
    name = input("Enter the name of the person to find: ")
    found_people = [person for person in people if person.name.lower() == name.lower()]
    if found_people:
        for person in found_people:
            print(person)
    else:
        print(f"No person found with the name '{name}'.")

def find_chore_by_task(people):
    task = input("Enter the task of the chore to find: ")
    found_chores = []
    for person in people:
        for chore in person.chores:
            if chore.task.lower() == task.lower():
                found_chores.append((person, chore))
    if found_chores:
        for person, chore in found_chores:
            print(f"Chore '{chore.task}' found for {person.name}.")
    else:
        print(f"No chore found with the task '{task}'.")