from Domain.event_domain import EntityList
from crud_ui import add_entity, modify_entity, delete_entity
from search_ui import search_entity

def exit_app(entity_list):
    print("-------------------------------------------")
    print("                 App closed                ")
    print("-------------------------------------------")
    exit()

def display_state(entity_list):
    print("The current app state is:")
    print(entity_list.get_person_list())
    print(entity_list.get_event_list())

menu = [(add_entity,"Add a person or an event"),
        (modify_entity,"Modify a person or an event"),
        (delete_entity,"Delete a person or an event"),
        (search_entity,"Search a person or an event"),
        ("","Subscribe a person to an event"),
        ("","Get reports"),
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