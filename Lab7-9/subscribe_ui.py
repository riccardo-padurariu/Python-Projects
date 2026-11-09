def subscribe_person(entity_list):
    print("You selected option 5: subscribe a person to an event")
    exit = input("If you want to go back to the main menu, type 'exit', else press Enter: ")
    if exit == 'exit':
        return
    print("\nThose are the current persons: ")
    entity_list.get_person_list().display()

    person_id = input("\nPlease enter the id of the person you want to subscribe(enter 'exit' to go back to the main menu): ")
    if person_id == "exit": return
    while entity_list.get_person_list().get_entity(person_id) is None:
        person_id = input("The id doesn't exist. Please enter again: ")
        if person_id == "exit": return

    selected_person = entity_list.get_person_list().get_entity(person_id)
    print("\nThe person selected is:")
    print(selected_person)

    print("\nThe events available are: ")
    entity_list.get_event_list().display()

    event_id = input("\nPlease enter the id of the event you want to subscribe the selected person(enter 'exit' to go back to the main menu): ")
    if event_id == "exit": return
    while entity_list.get_event_list().get_entity(event_id) is None:
        event_id = input("The id doesn't exist. Please enter again: ")
        if event_id == "exit": return

    selected_event = entity_list.get_event_list().get_entity(event_id)
    print("\nThe selected event is:")
    print(selected_event)

    confirmation = input("\nDo you want to finish the subscribe process?(Yes/No): ")
    if confirmation.lower() == "yes":
        selected_person.add_event(selected_event)
        selected_event.add_person(selected_person)
        print("\nPerson subscribed successfully!")
    else:
        print("\nProcess terminated")

