from seed import people
from helpers import (
    list_people,
    add_person,
    delete_person,
    update_person,
    list_chores,
    add_chore,
    delete_chore,
    update_chore,
    find_person_by_name,
    find_chore_by_task
)

def main_page():
    print("*********************************************************************")
    print("*                         📝 CHORES TRACKER 📝                     *")
    print("*********************************************************************")
    print("*                     Welcome to Chores List Tracker!               *")
    print("*********************************************************************")
    print("*                      Please choose from the following:            *")
    print("*********************************************************************")
    print("*                📝  Press V to View All People                    *")
    print("*                📝  Press M to Manage and View Chores             *")
    print("*                📝  Press E to Exit App                           *")
    print("---------------------------------------------------------------------")

def view_people(people):
    while True:
        list_people(people)
        print("*********************************************************************")
        print("*                        👪 MANAGE PEOPLE 👪                        *")
        print("*********************************************************************")
        print("*                Please choose from the following:                  *")
        print("*********************************************************************")
        print("*                  Press 1.  Add New Person                         *")
        print("*                  Press 2.  Delete a Person                        *")
        print("*                  Press 3.  Update a Person                        *")
        print("*                  Press 4.  Find a Person by Name                  *")
        print("*                  Press 5.  Back to Main Menu                      *")
        print("---------------------------------------------------------------------")

        choice = input("Enter your choice")
        if choice == '1':
            add_person(people)
        elif choice == '2':
            delete_person(people)
        elif choice == '3':
            update_person(people)
        elif choice == '4':
            find_person_by_name(people)
        elif choice == '5':
            break 
        else:
            print("Invalid choice, please try again")


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            helper_1()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Some useful function")


if __name__ == "__main__":
    main()
