from models.chore import Chore
from models.person import Person

def list_people():
    people = Person.get_all()
    for index, person in enumerate(people, start=1):
        print(f"{index}. {person.name} | Room: {person.room}")

def add_person():
    while True:
        name = input("Enter the person's name (or enter '.' to go back): ").strip()
        if name == '.':
            print("Returning to the previous menu.")
            return
        if not name:
            print("Name cannot be empty. Please enter a valid name.")
            continue
        if name.isdigit():
            print("Name cannot be a digit. Please enter a valid name.")
            continue
        if len(name) <= 1 or len(name) >= 15:
            print("Name must be greater than 1 character and less than 15 characters. Please enter a valid name.")
            continue
        while True:
            room = input("Enter the person's room (or enter '.' to go back): ").strip()
            if room == '.':
                print("Returning to the previous menu.")
                return
            if not room:
                print("Room cannot be empty. Please enter a valid room.")
            elif room.isdigit():
                print("Room cannot be all digits. Please enter a valid room.")
            else:
                break
        new_person = Person.create(name, room)
        new_person.save()
        print("***********************")
        print(f"Person '{name}' added.")
        print("***********************")
        break

def delete_person():
    list_people()
    all_people = Person.get_all()
    while True:
        user_input = input("Enter the number of the person to delete (or '.' to go back): ").strip()
        if user_input == '.':
            print("Returning to the previous menu.")
            return
        try:
            index = int(user_input) - 1
            if 0 <= index < len(all_people):
                deleted_person = all_people.pop(index)
                deleted_person.delete()
                print("***********************")
                print(f"Person '{deleted_person.name}' deleted.")
                print("***********************")
                break
            else:
                print("Invalid selection. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def update_person():
    list_people()
    all_people = Person.get_all()
    while True:
        user_input = input("Enter the number of the person to update (or '.' to go back): ").strip()
        if user_input == '.':
            print("Returning to the previous menu.")
            return
        try:
            index = int(user_input) - 1
            if 0 <= index < len(all_people):
                person = all_people[index]
                while True:
                    new_name = input(f"Enter new name for {person.name} (leave blank to keep current, or '.' to go back): ").strip()
                    if new_name == ".":
                        print("Returning to the previous menu.")
                        return
                    if new_name == "":
                        new_name = person.name
                        break
                    if new_name.isdigit():
                        print("Name cannot be all digits. Please enter a valid name.")
                        continue
                    if len(new_name) <= 1 or len(new_name) >= 20:
                        print("Name must be greater than 1 character and less than 20 characters.")
                        continue
                    person.name = new_name
                    break

                while True:
                    new_room = input(f"Enter new room for {person.room} (leave blank to keep current, or '.' to go back): ").strip()
                    if new_room == ".":
                        print("Returning to the previous menu.")
                        return
                    if new_room == "":
                        new_room = person.room
                        break
                    if new_room.isdigit():
                        print("Room cannot be all digits. Please enter a valid room.")
                        continue
                    person.room = new_room
                    break

                person.update()

                print("***********************")
                print(f"Person '{person.name}' updated.")
                print("***********************")
                break
            else:
                print("Invalid selection. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def list_chores():
    all_people = Person.get_all()
    for person in all_people:
        print("---------------------------------------------------------------------")
        print(f"{person.name} (Room: {person.room})")
        person_chores = person.chore()
        for index, chore in enumerate(person_chores):
            print(f"  {index + 1}. Task: {chore.task} | Status: {chore.status} | Priority: {chore.priority}")
        print("---------------------------------------------------------------------")

        
def add_chore():
    while True:
        all_people = Person.get_all()
        list_people()

        user_input = input("Enter the number of the person to add a chore for (or '.' to go back): ").strip()
        
        if user_input == ".":
            print("Returning to the previous menu.")
            return

        try:
            index = int(user_input) - 1
            if 0 <= index < len(all_people):
                person = all_people[index]
                
                while True:
                    task = input("Enter the task (or '.' to go back): ").strip()
                    if task == ".":
                        print("Returning to the previous menu.")
                        return
                    if len(task) < 2 or len(task) > 25:
                        print("Task must be at least 2 characters and less than 25 characters long.")
                    elif task.isdigit():
                        print("Task cannot be all digits. Please enter a valid task.")
                    else:
                        break

                while True:
                    status = input("Enter the status (Pending or Completed) (or '.' to go back): ").strip().capitalize()
                    if status == ".":
                        print("Returning to the previous menu.")
                        return
                    if status in ["Pending", "Completed"]:
                        break
                    else:
                        print("Invalid status. Please enter 'Pending' or 'Completed'.") 

                while True:
                    priority = input("Enter the priority (High, Medium, Low) (or '.' to go back): ").strip().capitalize()
                    if priority == ".":
                        print("Returning to the previous menu.")
                        return
                    if priority in ["High", "Medium", "Low"]:
                        break
                    else:
                        print("Invalid priority. Please enter 'High', 'Medium', or 'Low'.")

                chore = Chore(task=task, status=status, priority=priority, person_id=person.id)
                chore.save()
                print("***********************")
                print(f"Chore '{task}' added for {person.name}.")
                break
            else:
                print("Invalid selection. Please enter a valid number.")
        except ValueError:
            print("Invalid input: Please enter a valid number.")

def delete_chore():
    while True:
        all_people = Person.get_all()
        list_people()
        
        user_input = input("Enter the number of the person to delete a chore for (or '.' to go back): ").strip()
        if user_input == ".":
            print("Returning to the previous menu.")
            return
        try:
            person_index = int(user_input) - 1
            if 0 <= person_index < len(all_people):
                person = all_people[person_index]
                person_chores = person.chore()
                
                while True:
                    for index, chore in enumerate(person_chores):
                        print(f"  {index + 1}. Task: {chore.task} | Status: {chore.status} | Priority: {chore.priority}")
                    
                    user_input = input("Enter the number of the chore to delete (or '.' to go back): ").strip()
                    if user_input == ".":
                        print("Returning to the previous menu.")
                        break
                    try:
                        chore_index = int(user_input) - 1
                        if 0 <= chore_index < len(person_chores):
                            deleted_chore = person_chores[chore_index]
                            deleted_chore.delete()
                            print("***********************")
                            print(f"Chore '{deleted_chore.task}' deleted.")
                            print("***********************")
                            break
                        else:
                            print("Invalid selection. Please enter a valid number.")
                    except ValueError:
                        print("Invalid input. Please enter a number.")
                break
            else:
                print("Invalid selection. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def update_chore():
    while True:
        all_people = Person.get_all()
        list_people()
        
        person_input = input("Enter the number of the person to update a chore for (or '.' to go back): ").strip()
        if person_input == ".":
            return 
        try:
            person_index = int(person_input) - 1
            if 0 <= person_index < len(all_people):
                person = all_people[person_index]
                person_chores = person.chore()
                
                while True:
                    for index, chore in enumerate(person_chores):
                        print(f"  {index + 1}. Task: {chore.task} | Status: {chore.status} | Priority: {chore.priority}")
                    
                    chore_input = input("Enter the number of the chore to update (or '.' to go back): ").strip()
                    if chore_input == ".":
                        print("Returning to the previous menu.")
                        break
                    try:
                        chore_index = int(chore_input) - 1
                        if 0 <= chore_index < len(person_chores):
                            chore = person_chores[chore_index]
                            while True:
                                new_task = input(f"Enter new task name for {chore.task} (leave blank to keep current, or '.' to go back): ").strip()
                                if new_task == ".":
                                    print("Returning to the previous menu.")
                                    return
                                if new_task == "":
                                    new_task = chore.task
                                    break
                                if new_task.isdigit():
                                    print("Task cannot be all digits. Please enter a valid task.")
                                    continue
                                if len(new_task) <= 1 or len(new_task) >= 20:
                                    print("Task must be greater than 1 character and less than 20 characters.")
                                    continue
                                chore.task = new_task
                                break

                            while True:
                                new_status = input(f"Enter new status for {chore.status} (leave blank to keep current, or '.' to go back): ").strip().capitalize()
                                if new_status == ".":
                                    print("Returning to the previous menu.")
                                    return
                                if new_status == "":
                                    new_status = chore.status
                                    break
                                if new_status in ["Pending", "Completed"]:
                                    chore.status = new_status
                                    break
                                else:
                                    print("Invalid status. Please enter 'Pending' or 'Completed'.")

                            while True:
                                new_priority = input(f"Enter new priority for {chore.priority} (leave blank to keep current, or '.' to go back): ").strip().capitalize()
                                if new_priority == ".":
                                    print("Returning to the previous menu.")
                                    return
                                if new_priority == "":
                                    new_priority = chore.priority
                                    break
                                if new_priority in ["High", "Medium", "Low"]:
                                    chore.priority = new_priority
                                    break
                                else:
                                    print("Invalid priority. Please enter 'High', 'Medium', or 'Low'.")

                            chore.update()
                            print("***********************")
                            print(f"Chore '{chore.task}' updated.")
                            print("***********************")
                            break
                        else:
                            print("Invalid selection. Please enter a valid number.")
                    except ValueError:
                        print("Invalid input. Please enter a number.")
                return
            else:
                print("Invalid selection. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def find_person_by_name():
    name = input("Enter the name of the person to find (must be greater than 1 character) or enter '.' to go back: ").strip()
    
    if name == ".":
        print("Returning to the previous menu...")
        return

    if len(name) > 1:
        found_person = Person.find_by_name(name)
        if found_person:
            print("***********************")
            print(f"Name: {found_person.name} | Room: {found_person.room}")
            print("***********************")
        else:
            print(f"No person found with the name '{name}'.")
    else:
        print("Name must be greater than 1 character. Please try again.")


def find_chore_by_task():
    while True:
        task = input("Enter the task description to find (must be greater than 1 character) or enter '.' to go back: ").strip()
        
        if task == ".":
            print("Returning to the previous menu...")
            return
        if len(task) > 1:
            found_chore = Chore.find_by_task(task)
            if found_chore:
                person = Person.find_by_id(found_chore.person_id)
                print("***********************")
                print(f"Chore: {found_chore.task}")
                print(f"Assigned to: {person.name} (Room: {person.room})")
                print("***********************")
                return found_chore, person
            else:
                print(f"No chore found with the task '{task}'.")
        else:
            print("Task description must be greater than 1 character. Please try again.")
