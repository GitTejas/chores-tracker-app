# lib/helpers.py
from models.chore import Chore
from models.person import Person
from datetime import datetime

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
            print(f"  {index + 1}. Task: {chore.task} | Due: {chore.due_date} | Status: {chore.status} | Priority: {chore.priority}")
        print("---------------------------------------------------------------------")

def add_chore():
    pass

def delete_chore():
    pass

def update_chore():
    pass

def find_person_by_name():
    pass

def find_chore_by_task():
    pass


def exit_program():
    print("Goodbye!")
    exit()
