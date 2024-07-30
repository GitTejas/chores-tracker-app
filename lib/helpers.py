from models.chore import Chore
from models.person import Person

def list_people(people):
    for index, person in enumerate(people):
        print(f"{index + 1}. {person}")

def add_person(people):
    name = input("Enter the person's name: ")
    room = input("Enter the person's room: ")
    new_person = Person(name=name, room=room)
    new_person.save()  # Ensure the person is saved to the database
    people.append(new_person)
    print(f"Person '{name}' added.")

def delete_person(people):
    list_people(people)
    try:
        index = int(input("Enter the number of the person to delete: ")) - 1
        if 0 <= index < len(people):
            deleted_person = people.pop(index)
            deleted_person.delete()  # Ensure the person is deleted from the database
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
            new_name = input(f"Enter new name for {person.name} (leave blank to keep current): ")
            new_room = input(f"Enter new room for {person.room} (leave blank to keep current): ")
            if new_name:
                person.name = new_name
            if new_room:
                person.room = new_room
            person.save()  # Ensure the person is updated in the database
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
            
            status = input("Enter the status: ")
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
        print(f"Invalid input: {ve}. Please enter a valid number.")




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
                deleted_chore.delete()  # Ensure the chore is deleted from the database
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
                new_task = input(f"Enter new task for '{chore.task}' (leave blank to keep current): ")
                new_status = input(f"Enter new status for '{chore.status}' (leave blank to keep current): ")
                new_priority = input(f"Enter new priority for '{chore.priority}' (leave blank to keep current): ")

                if new_task:
                    chore.task = new_task
                if new_status:
                    chore.status = new_status
                if new_priority:
                    chore.priority = new_priority

                chore.save()  # Ensure the chore is updated in the database
                print(f"Chore '{chore.task}' updated.")
            else:
                print("Invalid selection.")
        else:
            print("Invalid selection.")
    except ValueError:
        print("Invalid input. Please enter a number.")



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