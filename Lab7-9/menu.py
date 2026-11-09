from Domain.event_domain import EntityList
from crud_ui import add_entity, modify_entity, delete_entity
from search_ui import search_entity
from subscribe_ui import subscribe_person

def exit_app(entity_list):
    print("-------------------------------------------")
    print("                 App closed                ")
    print("-------------------------------------------")
    exit()

def display_state(entity_list):
    print("The current app state is:")
    print(entity_list.get_person_list())
    print(entity_list.get_event_list())

def get_person(person_list):
    if not person_list:
        print("No persons available")
        return
    person_id = input("Please enter the id of the person you want to search(type 'exit' to go back): ")
    if person_id == "exit": return
    while person_list.get_entity(person_id) is None:
        person_id = input("The id doesn't exist. Please enter again(or 'exit' to go back): ")
        if person_id == "exit": return

    print(f"The person with the ID {person_id} is:")
    print(person_list.get_entity(person_id))

def get_event(event_list):
    if not event_list:
        print("No events available")
        return
    event_id = input("Please enter the id of the event you want to search(type 'exit' to go back): ")
    if event_id == "exit": return
    while event_list.get_entity(event_id) is None:
        event_id = input("The id doesn't exist. Please enter again(or 'exit' to go back): ")
        if event_id == "exit": return

    print(f"The event with the ID {event_id} is:")
    print(event_list.get_entity(event_id))


def get_info(entity_list):
    print("You can get the following info:")
    print("1. A person data")
    print("2. An event data")
    option = input("Please enter the option you want to get the info from: ")
    while not option.isdigit() or (option.isdigit() and (int(option) not in [1,2])):
        option = input("The option must be an integer between 1 and 2. Please enter again: ")

    if option == "1":
        get_person(entity_list.get_person_list())
    elif option == "2":
        get_event(entity_list.get_event_list())

menu = [(add_entity,"Add a person or an event"),
        (modify_entity,"Modify a person or an event"),
        (delete_entity,"Delete a person or an event"),
        (search_entity,"Search a person or an event"),
        (subscribe_person,"Subscribe a person to an event"),
        ("","Get reports"),
        (get_info,"Get info"),
        (display_state,"Get current app state"),
        (exit_app,"Exit app")]


def display_menu():
    print("------------------------------------")
    print("Welcome to the event manager system!")
    print("------------------------------------")

    entity_list = EntityList()

    while True:
        for index, i in enumerate(menu):
            print(f"Option {index+1}. {i[1]}")

        option = input(f"Please select an option from 1 to {len(menu)}: ")
        while not option.isdigit() or (option.isdigit() and (int(option) < 1 or int(option) > len(menu))):
            option = input(f"The option must be an integer between 1 and {len(menu)}. Please enter again the option: ")

        option = int(option)

        print()
        menu[option-1][0](entity_list)
        print()