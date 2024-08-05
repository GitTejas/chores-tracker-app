from models.chore import Chore
from models.person import Person

def list_people(people):
    people = Person.get_all()
    for index, person in enumerate(people):
        print(f"{index + 1}. {person}")

def add_person(people):
    while True:
        # Prompt user for name with option to go back
        name = input("Enter the person's name (or enter '.' to go back): ").strip()
        if name == '.':
            print("Returning to the previous menu.")
            return  # Exit function and return to previous menu
        
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
            # Prompt user for room with option to go back
            room = input("Enter the person's room (or enter '.' to go back): ").strip()
            if room == '.':
                print("Returning to the previous menu.")
                return  # Exit function and return to previous menu
            
            if not room:
                print("Room cannot be empty. Please enter a valid room.")
            elif room.isdigit():
                print("Room cannot be all digits. Please enter a valid room.")
            else:
                break
        
        new_person = Person.create(name, room)
        new_person.save()
        people.append(new_person)
        print(f"Person '{name}' added.")
        break


def delete_person(people):
    list_people(people)
    while True:
        # Prompt user for index with option to go back
        user_input = input("Enter the number of the person to delete (or '.' to go back): ").strip()
        if user_input == '.':
            print("Returning to the previous menu.")
            return  # Exit function and return to previous menu
        try:
            index = int(user_input) - 1
            if 0 <= index < len(people):
                deleted_person = people.pop(index)
                deleted_person.delete()
                print(f"Person '{deleted_person.name}' deleted.")
                break
            else:
                print("Invalid selection. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")



def update_person(people):
    list_people(people)
    while True:
        user_input = input("Enter the number of the person to update (or '.' to go back): ").strip()
        if user_input == '.':
            print("Returning to the previous menu.")
            return  # Exit function and return to previous menu
        try:
            index = int(user_input) - 1
            if 0 <= index < len(people):
                person = people[index]
                while True:
                    new_name = input(f"Enter new name for {person.name} (leave blank to keep current, or '.' to go back): ").strip()
                    if new_name == ".":
                        print("Returning to the previous menu.")
                        return  # Exit function and return to previous menu
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
                        return  # Exit function and return to previous menu
                    if new_room == "":
                        new_room = person.room
                        break
                    if new_room.isdigit():
                        print("Room cannot be all digits. Please enter a valid room.")
                        continue
                    person.room = new_room
                    break
                person.save()
                print(f"Person '{person.name}' updated.")
                break
            else:
                print("Invalid selection. Please enter a valid number.")
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
    while True:
        list_people(people)
        user_input = input("Enter the number of the person to add a chore for (or '.' to go back): ").strip()
        
        if user_input == ".":
            print("Returning to the previous menu.")
            return  # Exit function and return to the previous menu
        
        try:
            index = int(user_input) - 1
            if 0 <= index < len(people):
                person = people[index]
                
                while True:
                    task = input("Enter the task (or '.' to go back): ").strip()
                    if task == ".":
                        print("Returning to the previous menu.")
                        return  # Exit function and return to the previous menu
                    if len(task) < 2 or len(task) > 25:
                        print("Task must be at least 2 characters and less than 25 characters long.")
                    elif task.isdigit():
                        print("Task cannot be all digits. Please enter a valid task.")
                    else:
                        break
                
                while True:
                    status = input("Enter the status (Pending or Completed) (or '.' to go back): ")
                    if status == ".":
                        print("Returning to the previous menu.")
                        return  # Exit function and return to the previous menu
                    if status in ["Pending", "Completed"]:
                        break
                    else:
                        print("Invalid status. Please enter 'Pending' or 'Completed'.")
                
                while True:
                    priority = input("Enter the priority (High, Medium, Low) (or '.' to go back): ")
                    if priority == ".":
                        print("Returning to the previous menu.")
                        return  # Exit function and return to the previous menu
                    if priority in ["High", "Medium", "Low"]:
                        break
                    else:
                        print("Invalid priority. Please enter 'High', 'Medium', or 'Low'.")
                
                chore = Chore(task=task, status=status, priority=priority, person_id=person.id)
                person.add_chore(chore)
                print(f"Chore '{task}' added for {person.name}.")
                break
            else:
                print("Invalid selection. Please enter a valid number.")
        except ValueError:
            print("Invalid input: Please enter a valid number.")


def delete_chore(people):
    while True:
        list_people(people)
        user_input = input("Enter the number of the person to delete a chore for (or '.' to go back): ").strip()
        
        if user_input == ".":
            print("Returning to the previous menu.")
            return  # Exit function and return to the previous menu

        try:
            person_index = int(user_input) - 1
            if 0 <= person_index < len(people):
                person = people[person_index]
                while True:
                    # Display the chores
                    for index, chore in enumerate(person.chores):
                        print(f"  {index + 1}. {chore}")

                    # Prompt for chore selection
                    user_input = input("Enter the number of the chore to delete (or '.' to go back): ").strip()
                    
                    if user_input == ".":
                        print("Returning to the previous menu.")
                        break  # Exit inner loop to go back to the person selection
                    
                    try:
                        chore_index = int(user_input) - 1
                        if 0 <= chore_index < len(person.chores):
                            deleted_chore = person.chores.pop(chore_index)
                            deleted_chore.delete()
                            print(f"Chore '{deleted_chore.task}' deleted.")
                            break
                        else:
                            print("Invalid selection. Please enter a valid number.")
                    except ValueError:
                        print("Invalid input. Please enter a number.")
                # Break the outer loop to return to the main menu after handling chores
                break
            else:
                print("Invalid selection. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")



def update_chore(people):
    while True:
        list_people(people)
        try:
            person_index = int(input("Enter the number of the person to update a chore for: ")) - 1
            if 0 <= person_index < len(people):
                person = people[person_index]
                while True:
                    for index, chore in enumerate(person.chores):
                        print(f"  {index + 1}. {chore}")
                    try:
                        chore_index = int(input("Enter the number of the chore to update: ")) - 1
                        if 0 <= chore_index < len(person.chores):
                            chore = person.chores[chore_index]

                            new_task = input(f"Enter new task for '{chore.task}' (leave blank to keep current): ").strip()
                            if new_task:
                                chore.task = new_task
                            
                            while True:
                                new_status = input(f"Enter new status for '{chore.status}' (leave blank to keep current): ").strip()
                                if new_status in ["Pending", "Completed", ""]:
                                    if new_status:
                                        chore.status = new_status
                                    break
                                else:
                                    print("Invalid status. Please enter 'Pending' or 'Completed'.")

                            while True:
                                new_priority = input(f"Enter new priority for '{chore.priority}' (leave blank to keep current): ").strip()
                                if new_priority in ["High", "Medium", "Low", ""]:
                                    if new_priority:
                                        chore.priority = new_priority
                                    break
                                else:
                                    print("Invalid priority. Please enter 'High', 'Medium', or 'Low'.")

                            chore.save()
                            print(f"Chore '{chore.task}' updated.")
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

def find_person_by_id(person_id):
    person = Person.find_by_id(person_id)
    if person:
        return person
    else:
        print("Person not found.")
        return None

def find_chore_by_id(chore_id):
    chore = Chore.find_by_id(chore_id)
    if chore:
        return chore
    else:
        print("Chore not found.")
        return None

def find_person_by_id():
    while True:
        user_input = input("Enter the ID of the person to find (or '.' to go back): ").strip()
        if user_input == ".":
            print("Returning to the previous menu.")
            return  # Exit function and return to previous menu
        try:
            person_id = int(user_input)
            person = Person.find_by_id(person_id)
            if person:
                print(person)
                return person
            else:
                print(f"No person found with ID '{person_id}'.")
        except ValueError:
            print("Invalid ID. Please enter a valid integer.")


def find_chore_by_id():
    while True:
        user_input = input("Enter the ID of the chore to find (or '.' to go back): ").strip()
        if user_input == ".":
            print("Returning to the previous menu.")
            return  # Exit function and return to previous menu
        try:
            chore_id = int(user_input)
            chore = Chore.find_by_id(chore_id)
            if chore:
                person = Person.find_by_id(chore.person_id)
                if person:
                    print(f"Chore '{chore.task}' found for {person.name}.")
                else:
                    print(f"Chore '{chore.task}' found, but no person associated with this chore.")
                return chore
            else:
                print(f"No chore found with ID '{chore_id}'.")
        except ValueError:
            print("Invalid ID. Please enter a valid integer.")

