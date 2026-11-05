from Domain.person_domain import Person
from crud_business import valid_date
from Domain.event_domain import Event
from crud_business import get_id

def get_name():

    input_name = input("Please enter the name and the surname(separated by one space): ")
    while len(input_name.split()) != 2:
        input_name = input("You must enter the name and the surname separated by one space(If you have more surnames, separate them with a '-'). Please enter again: ")

    return input_name

def get_address():

    address = input("Please enter the address: ")
    while address == "":
        address = input("The address must be non-empty. Please enter again: ")

    return address

def get_date():

    date = input(f"Enter the event date(dd/mm/yyyy): ")
    condition, feedback = valid_date(date)
    while not condition:
        date = input(f"The event date must {feedback}. Please enter again the event date(dd/mm/yyyy): ")
        condition, feedback = valid_date(date)

    return date


def get_duration():

    duration = input("Please enter the duration of the event(minutes): ")

    while not duration.isdigit():
        duration = input("The duration must be an integer. Please enter the duration again(minutes): ")

    return int(duration)


def get_description():
    description = input("Please enter the description of the event: ")

    while description == "":
        description = input("The description must be non-empty. Please enter again: ")

    return description


def validate_input(entity_type):

    if entity_type == "person":
        person_id = get_id()
        name = get_name()
        address = get_address()

        return person_id, name, address
    elif entity_type == "event":
        event_id = get_id()
        date = get_date()
        duration = get_duration()
        description = get_description()

        return event_id, date, duration, description

    return None

def add_person(person_list):

    print("You selected the option to add a new person")
    person_id, name, address = validate_input("person")
    person = Person(person_id, name, address)
    person_list.add_person(person)
    print("The following person was added:")
    print(person)
    print("The current persons are:")
    person_list.display()

def add_event(event_list):
    print("You selected the option to add a new event")
    event_id, date, duration, description = validate_input("event")
    event = Event(event_id, date, duration, description)
    event_list.add_event(event)
    print("The following event was added:")
    print(event)
    print("The current events are:")
    event_list.display()


def add_entity(entity_list):
    print("You selected option 1: adding a person or an event")
    exit = input("If you want to go back to the main menu, press 5, else press Enter: ")
    if exit == 5:
        return
    print("You can add: ")
    print("1. A person")
    print("2. An event")
    option = input("Please enter the option you want to choose: ")
    while not option.isdigit() or (option.isdigit() and (int(option) < 1 or int(option) > 2)):
        option = input("The option must be an integer between 1 and 2. Please enter again: ")

    if option == "1":
        add_person(entity_list.get_person_list())
    elif option == "2":
        add_event(entity_list.get_event_list())

def get_modify_id(param_list, status):
    print(f"The current {status} are:")
    param_list.display()

    param_id = input("Please enter the id you want to modify: ")
    while param_list.get_entity(param_id) is None:
        param_id = input("The id doesn't exist. Please enter again: ")

    return param_id

def modify_person(person_list):

    if not person_list:
        print("No persons available for modification")
        return

    print("You selected to modify a person")

    person_id = get_modify_id(person_list, "persons")


    print("You can modify the following attributes:")
    print("1. Name")
    print("2. Address")
    option = input("Please enter the option you want to choose: ")
    while not option.isdigit() or (option.isdigit() and (int(option) < 1 or int(option) > 2)):
        option = input("The option must be an integer between 1 and 2. Please enter again: ")

    if option == "1":
        new_name = get_name()
        person_list.set_attribute(person_id,"name",new_name)
    elif option == "2":
        new_address = get_address()
        person_list.set_attribute(person_id,"address",new_address)

    print("The person was modified successfully! Here is the modified person: ")
    print(person_list.get_entity(person_id))

def modify_event(event_list):

    if not event_list:
        print("No events available for modification")
        return

    print("You selected to modify an event")

    event_id = get_modify_id(event_list, "events")

    print("You can modify the following attributes:")
    print("1. Date")
    print("2. Duration")
    print("3. Description")
    option = input("Please enter the option you want to choose: ")
    while not option.isdigit() or (option.isdigit() and (int(option) < 1 or int(option) > 3)):
        option = input("The option must be an integer between 1 and 3. Please enter again: ")

    if option == "1":
        new_date = get_date()
        event_list.set_attribute(event_id, "date", new_date)
    elif option == "2":
        new_duration = get_duration()
        event_list.set_attribute(event_id, "duration", new_duration)
    elif option == "3":
        new_description = get_description()
        event_list.set_attribute(event_id, "description", new_description)

    print("The event was modified successfully! Here is the modified event: ")
    print(event_list.get_entity(event_id))


def modify_entity(entity_list):
    print("You selected option 2: modifying a person or an event")
    exit = input("If you want to go back to the main menu, press 5, else press Enter: ")
    if exit == 5:
        return
    print("You can modify: ")
    print("1. A person")
    print("2. An event")
    option = input("Please enter the option you want to choose: ")
    while not option.isdigit() or (option.isdigit() and (int(option) < 1 or int(option) > 2)):
        option = input("The option must be an integer between 1 and 2. Please enter again: ")

    if option == "1":
        modify_person(entity_list.get_person_list())
    elif option == "2":
        modify_event(entity_list.get_event_list())


def delete_person(person_list):
    if not person_list:
        print("No persons to delete")
        return

    print("These are the current persons:")
    person_list.display()
    person_id = input("\nPlease select the id you want to delete: ")
    while person_list.get_entity(person_id) is None:
        person_id = input("The id doesn't exist. Please enter again: ")
    person_list.delete(person_id)

    print("Person deleted successfully!")

def delete_event(event_list):
    if not event_list:
        print("No events to delete")
        return

    print("These are the current persons:")
    event_list.display()
    event_id = input("\nPlease select the id you want to delete: ")
    while event_list.get_entity(event_id) is None:
        event_id = input("The id doesn't exist. Please enter again: ")
    event_list.delete(event_id)

    print("Event deleted successfully!")


def delete_entity(entity_list):
    print("You selected option 3: deleting a person or an event")
    exit = input("If you want to go back to the main menu, press 5, else press Enter: ")
    if exit == 5:
        return
    print("You can delete: ")
    print("1. A person")
    print("2. An event")
    option = input("Please enter the option you want to choose: ")
    while not option.isdigit() or (option.isdigit() and (int(option) < 1 or int(option) > 2)):
        option = input("The option must be an integer between 1 and 2. Please enter again: ")

    if option == "1":
        delete_person(entity_list.get_person_list())
    elif option == "2":
        delete_event(entity_list.get_event_list())