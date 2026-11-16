from reports_business import sort_by, calculate, get_top_20_events, date, description

def generate_sorted_list(person_list):
    print("You selected to generate a sorted list with the events a specific person is attending to")
    print("You can sort by:")
    print("1. Description")
    print("2. Date")

    option = input("Please enter the option corresponding to the criteria you want to sort by: ")
    while not option.isdigit() or (option.isdigit() and (int(option) < 1 or int(option) > 2)):
        option = input("The option must be an integer between 1 and 2. Please enter again: ")

    person_id = input("Please enter the id of the person you want to generate the report: ")
    while person_list.get_entity(person_id) is None:
        person_id = input("The id doesn't exist. Please enter again: ")

    selected_person = person_list.get_entity(person_id)

    print(selected_person)

    sorted_list = []


    if option == "1":
        sorted_list = sort_by(selected_person.get_events(), description)
    elif option == "2":
        sorted_list = sort_by(selected_person.get_events(), date)

    print(sorted_list)
    criteria = "description" if option == 1 else "date"
    print(f"The sorted list based on the {criteria} is: ")
    for event in sorted_list:
        print(event)

def calculate_max_events(person_list):
    max_persons = calculate(person_list)
    is_list = isinstance(max_persons, list)
    print(f"The person{'s' if is_list else ''} that participate to the most events {'are' if is_list else 'is'}: ")
    if is_list:
        for person in max_persons: print(person)
    else:
        print(max_persons)

def get_top_20(event_list):
    print("The top 20% of the events that have the most participants are: ")
    top_20_list = get_top_20_events(event_list)
    for event in top_20_list:
        print(event)

def generate_reports(entity_list):
    print("You selected option 6: Generating reports")

    exit = input("If you want to go back to the main menu, type 'exit', otherwise press Enter: ")
    if exit.lower() == "exit":
        return

    print("You can generate 3 reports:")
    print("1. Sorted list with the events a specific person is attending to")
    print("2. The persons that joined the most events")
    print("3. The first 20% of the events with the most participants")

    option = input("Please enter the option you want to select: ")
    while not option.isdigit() or (option.isdigit() and (int(option) < 1 or int(option) > 3)):
        option = input("The option must be an integer between 1 and 3. Please enter again: ")

    if option == "1":
        generate_sorted_list(entity_list.get_person_list())
    elif option == "2":
        calculate_max_events(entity_list.get_person_list())
    elif option == "3":
        get_top_20(entity_list.get_event_list())
