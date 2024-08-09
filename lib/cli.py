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

def view_people():
    while True:
        list_people()
        print("*********************************************************************")
        print("*                        👪 MANAGE PEOPLE 👪                        *")
        print("*********************************************************************")
        print("*                Please choose from the following:                  *")
        print("*********************************************************************")
        print("*                  Press 1.  Add New Person                         *")
        print("*                  Press 2.  Delete a Person                        *")
        print("*                  Press 3.  Update a Person                        *")
        print("*                  Press 4.  Find a Person by Name                  *")
        print("*                  Press 5.  Manage Chores                          *")
        print("*                  Press 6.  Back to Main Menu                      *")
        print("---------------------------------------------------------------------")

        choice = input("Enter your choice: ")
        if choice == '1':
            add_person()
        elif choice == '2':
            delete_person()
        elif choice == '3':
            update_person()
        elif choice == '4':
            find_person_by_name()
        elif choice == '5':
            manage_chores()  
        elif choice == '6':
            main()
        else:
            print("Invalid choice, please try again.")

def manage_chores():
    while True:
        print("*********************************************************************")
        print("*                         🗓️  MANAGE CHORES 🗓️                        *")
        print("*********************************************************************")
        print("*                Please choose from the following:                  *")
        print("*********************************************************************")
        print("*                  Press 1.  View All Chores                        *")
        print("*                  Press 2.  Add New Chore                          *")
        print("*                  Press 3.  Delete a Chore                         *")
        print("*                  Press 4.  Update a Chore                         *")
        print("*                  Press 5.  Find a Chore by Task                   *")
        print("*                  Press 6.  View People                            *")
        print("*                  Press 7.  Back to Main Menu                      *")
        print("---------------------------------------------------------------------")

        choice = input("Enter your choice: ")
        if choice == '1':
            list_chores()
        elif choice == '2':
            add_chore()
        elif choice == '3':
            delete_chore()
        elif choice == '4':
            update_chore()
        elif choice == '5':
            find_chore_by_task()
        elif choice == '6':
            view_people() 
        elif choice == '7':
            main()
        else:
            print("Invalid choice, please try again.")

def exit_program():
    print("Exiting the app. Good Day!")
    exit()

def main():
    while True:
        main_page()
        choice = input("> ").lower()
        if choice == 'v':
            view_people()
        elif choice == 'm':
            manage_chores()
        elif choice == 'e':
            exit_program()
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
