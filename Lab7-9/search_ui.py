def get_criteria(entity_type):
    if entity_type == "person":
        print("1. Name")
        print("2. Address")
        print("3. ID")
        options = ["name", "address", "id"]

        criteria = input("Please enter the attribute you want to search(type 'exit' to go back): ")
        if criteria == "exit": return "exit"
        while not criteria.isdigit() or (criteria.isdigit() and (int(criteria) < 1 or int(criteria) > 3)):
            criteria = input("The option must be an integer between 1 and 2. Please enter again(type 'exit' to go back): ")
            if criteria == "exit": return "exit"

        return options[int(criteria)-1]

    elif entity_type == "event":
        print("1. Date")
        print("2. Duration")
        print("3. Description")
        print("4. ID")
        options = ["date","duration","description","id"]

        criteria = input("Please enter the attribute you want to search(type 'exit' to go back): ")
        if criteria == "exit": return "exit"
        while not criteria.isdigit() or (criteria.isdigit() and (int(criteria) < 1 or int(criteria) > 4)):
            criteria = input("The option must be an integer between 1 and 3. Please enter again(type 'exit' to go back): ")
            if criteria == "exit": return "exit"

        return options[int(criteria)-1]


def search_person(person_list):
    print("You selected to search for a person")

    criteria = get_criteria("person")
    if criteria == "exit":
        return
    input_search = input("Enter the person you want to search: ")

    condition, search_result = person_list.search_by_criteria(criteria, input_search)

    if not search_result:
        print("No person found with the criteria and the search input entered")
    else:
        print(f"The search result for the input {input_search}")
        for person in search_result:
            print(person)
    while criteria != "exit":
        criteria = get_criteria("person")
        if criteria == "exit":
            return
        input_search = input("Enter the person you want to search: ")

        condition, search_result = person_list.search_by_criteria(criteria, input_search)

        if not search_result:
            print("No person found with the criteria and the search input entered")
        else:
            print(f"The search result for the input {input_search}")
            for person in search_result:
                print(person)

def search_event(event_list):
    print("You selected to search for an event")

    criteria = get_criteria("event")
    if criteria == "exit":
        return
    input_search = input("Enter the event you want to search: ")

    condition, search_result = event_list.search_by_criteria(criteria, input_search)

    if not search_result:
        print("No event found with the criteria and the search input entered")
    else:
        print(f"The search result for the input {input_search}")
        for event in search_result:
            print(event)
    while criteria != "exit":
        criteria = get_criteria("event")
        if criteria == "exit":
            return
        input_search = input("Enter the event you want to search: ")

        condition, search_result = event_list.search_by_criteria(criteria, input_search)

        if not search_result:
            print("No event found with the criteria and the search input entered")
        else:
            print(f"The search result for the input {input_search}")
            for event in search_result:
                print(event)

def search_entity(entity_list):
    print("You selected option 4: searching a person or an event")
    exit = input("If you want to go back to the main menu, press 5, else press Enter: ")
    if exit == 5:
        return
    while True:
        print("You can search: ")
        print("1. A person")
        print("2. An event")
        option = input("Please enter the option you want to search(type 'exit' to return to the main menu): ")
        if option == "exit":
            return
        while not option.isdigit() or (option.isdigit() and (int(option) < 1 or int(option) > 2)):
            option = input("The option must be an integer between 1 and 2(or 'exit' to return to the main menu). Please enter again: ")
            if option == "exit":
                return

        if option == "1":
            search_person(entity_list.get_person_list())
        elif option == "2":
            search_event(entity_list.get_event_list())