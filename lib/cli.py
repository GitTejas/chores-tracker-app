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
