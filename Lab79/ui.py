import random
from email.encoders import encode_base64

from Lab79.Domain.event import Event
from Lab79.Domain.person import Person


class UI:
    """
    The class that implements the UI
    """
    def __init__(self, person_service, event_service):
        self.__service = {
            "person_service": person_service,
            "event_service": event_service
        }

    def get_person_service(self):
        """
        Returns the person_service
        :return: Service
        """
        return self.__service["person_service"]

    def get_event_service(self):
        """
        Returns the event_service
        :return: Service
        """
        return self.__service["event_service"]

    @staticmethod
    def get_name():
        """
        Returns a valid name given by the user
        :return: str
        """
        input_name = input("Please enter the name and the surname(separated by one space): ")
        while len(input_name.split()) != 2:
            input_name = input(
                "You must enter the name and the surname separated by one space(If you have more surnames, separate them with a '-'). Please enter again: ")

        return input_name

    @staticmethod
    def get_address():
        """
        Returns a valid address given by the user
        :return: str
        """
        address = input("Please enter the address: ")
        while address == "":
            address = input("The address must be non-empty. Please enter again: ")

        return address

    def get_date(self):
        """
        Returns a valid date given by the user
        :return: str
        """
        date = input(f"Enter the event date(dd/mm/yyyy): ")
        condition, feedback = self.get_person_service().valid_date(date)
        while not condition:
            date = input(f"The event date must {feedback}. Please enter again the event date(dd/mm/yyyy): ")
            condition, feedback = self.get_person_service().valid_date(date)

        return date

    @staticmethod
    def get_duration():
        """
        Returns a valid duration given by the user
        :return: int
        """
        duration = input("Please enter the duration of the event(minutes): ")

        while not duration.isdigit():
            duration = input("The duration must be an integer. Please enter the duration again(minutes): ")

        return int(duration)

    @staticmethod
    def get_description():
        """
        Returns a valid description given by the user
        :return: str
        """
        description = input("Please enter the description of the event: ")

        while description == "":
            description = input("The description must be non-empty. Please enter again: ")

        return description

    def validate_input(self, entity_type):
        """
        Based on the entity_type, returns a valid input set
        :param entity_type: str
        :return: tuple(str, str, str) | tuple(str, str, int, str) | None
        """
        if entity_type == "person":
            person_id = self.get_person_service().get_id()
            name = self.get_name()
            address = self.get_address()

            return person_id, name, address
        elif entity_type == "event":
            event_id = self.get_event_service().get_id()
            date = self.get_date()
            duration = self.get_duration()
            description = self.get_description()

            return event_id, date, duration, description

        return None

    def get_modify_id(self, status):
        """
        Based on the status, returns a valid id given by the user
        :param status: str
        :return: str
        """
        param_service = self.get_person_service().get_repository() if status == "persons" else self.get_event_service().get_repository()
        print(f"The current {status} are:")
        param_service.display()

        param_id = input("Please enter the id you want to modify: ")
        while param_service.get_element(param_id) is None:
            param_id = input("The id doesn't exist. Please enter again: ")

        return param_id

    def add_person(self):
        """
        Adds a person to the corresponding repository
        :return: None
        """
        person_service = self.get_person_service()
        print("You selected the option to add a new person")
        person_id, name, address = self.validate_input("person")
        person = Person(person_id, name, address)
        person_service.add(person)
        print("The following person was added:")
        print(person)
        print("The current persons are:")
        person_service.display()

    def add_event(self):
        """
        Adds an event to the corresponding repository
        :return: None
        """
        event_service = self.get_event_service()
        print("You selected the option to add a new event")
        event_id, date, duration, description = self.validate_input("event")
        event = Event(event_id, date, duration, description)
        event_service.add(event)
        print("The following event was added:")
        print(event)
        print("The current events are:")
        event_service.display()

    def add(self):
        """
        The method that implements the add functionality
        :return: None
        """
        print("You selected option 1: adding a person or an event")
        exit_app = input("If you want to go back to the main menu, type 'exit', else press Enter: ")
        if exit_app == "exit":
            return
        print("You can add: ")
        print("1. A person")
        print("2. An event")
        option = input("Please enter the option you want to choose: ")
        while not option.isdigit() or (option.isdigit() and (int(option) < 1 or int(option) > 2)):
            option = input("The option must be an integer between 1 and 2. Please enter again: ")

        if option == "1":
            self.add_person()
        elif option == "2":
            self.add_event()

    def modify_person(self):
        """
        Modifies a person
        :return: None
        """
        if not self.get_person_service().get_repository().get_elements():
            print("No persons available for modification")
            return

        print("You selected to modify a person")

        person_id = self.get_modify_id("persons")

        print("You can modify the following attributes:")
        print("1. Name")
        print("2. Address")
        option = input("Please enter the option you want to choose: ")
        while not option.isdigit() or (option.isdigit() and (int(option) < 1 or int(option) > 2)):
            option = input("The option must be an integer between 1 and 2. Please enter again: ")

        if option == "1":
            new_name = self.get_name()
            self.get_person_service().get_repository().set_attribute(person_id, "name", new_name)
        elif option == "2":
            new_address = self.get_address()
            self.get_person_service().get_repository().set_attribute(person_id, "address", new_address)

        print("The person was modified successfully! Here is the modified person: ")
        print(self.get_person_service().get_repository().get_element(person_id))

    def modify_event(self):
        """
        Modifies an event
        :return: None
        """
        if not self.get_event_service().get_repository().get_elements():
            print("No events available for modification")
            return

        print("You selected to modify an event")

        event_id = self.get_modify_id("events")

        print("You can modify the following attributes:")
        print("1. Date")
        print("2. Duration")
        print("3. Description")
        option = input("Please enter the option you want to choose: ")
        while not option.isdigit() or (option.isdigit() and (int(option) < 1 or int(option) > 3)):
            option = input("The option must be an integer between 1 and 3. Please enter again: ")

        if option == "1":
            new_date = self.get_date()
            self.get_event_service().get_repository().set_attribute(event_id, "date", new_date)
        elif option == "2":
            new_duration = self.get_duration()
            self.get_event_service().get_repository().set_attribute(event_id, "duration", new_duration)
        elif option == "3":
            new_description = self.get_description()
            self.get_event_service().get_repository().set_attribute(event_id, "description", new_description)

        print("The event was modified successfully! Here is the modified event: ")
        print(self.get_event_service().get_repository().get_element(event_id))

    def modify(self):
        """
        The method that implements the modify functionality
        :return: None
        """
        print("You selected option 2: modifying a person or an event")
        exit_app = input("If you want to go back to the main menu, type 'exit', else press Enter: ")
        if exit_app == "exit":
            return
        print("You can modify: ")
        print("1. A person")
        print("2. An event")
        option = input("Please enter the option you want to choose: ")
        while not option.isdigit() or (option.isdigit() and (int(option) < 1 or int(option) > 2)):
            option = input("The option must be an integer between 1 and 2. Please enter again: ")

        if option == "1":
            self.modify_person()
        elif option == "2":
            self.modify_event()

    def delete_person(self):
        """
        Deletes a person
        :return: None
        """
        if not self.get_person_service().get_repository().get_elements():
            print("No persons to delete")
            return

        print("These are the current persons:")
        self.get_person_service().get_repository().display()
        person_id = input("\nPlease select the id you want to delete: ")
        while self.get_person_service().get_repository().get_element(person_id) is None:
            person_id = input("The id doesn't exist. Please enter again: ")
        self.get_person_service().delete(person_id)

        print("Person deleted successfully!")

    def delete_event(self):
        """
        Deletes an event
        :return: None
        """
        if not self.get_event_service().get_repository().get_elements():
            print("No events to delete")
            return

        print("These are the current events:")
        self.get_event_service().get_repository().display()
        event_id = input("\nPlease select the id you want to delete: ")
        while self.get_event_service().get_repository().get_element(event_id) is None:
            event_id = input("The id doesn't exist. Please enter again: ")
        self.get_event_service().delete(event_id)

        print("Event deleted successfully!")

    def delete(self):
        """
        The method that implements the delete functionality
        :return: None
        """
        print("You selected option 3: deleting a person or an event")
        exit_app = input("If you want to go back to the main menu, type 'exit', else press Enter: ")
        if exit_app == "exit":
            return
        print("You can delete: ")
        print("1. A person")
        print("2. An event")
        option = input("Please enter the option you want to choose: ")
        while not option.isdigit() or (option.isdigit() and (int(option) < 1 or int(option) > 2)):
            option = input("The option must be an integer between 1 and 2. Please enter again: ")

        if option == "1":
            self.delete_person()
        elif option == "2":
            self.delete_event()

    @staticmethod
    def get_criteria(entity_type):
        """
        Based on the entity_type, returns a valid criteria given by the user
        :param entity_type: str
        :return: str
        """
        if entity_type == "person":
            print("1. Name")
            print("2. Address")
            print("3. ID")
            options = ["name", "address", "id"]

            criteria = input("Please enter the attribute you want to search(type 'exit' to go back): ")
            if criteria == "exit": return "exit"
            while not criteria.isdigit() or (criteria.isdigit() and (int(criteria) < 1 or int(criteria) > 3)):
                criteria = input(
                    "The option must be an integer between 1 and 2. Please enter again(type 'exit' to go back): ")
                if criteria == "exit": return "exit"

            return options[int(criteria) - 1]

        elif entity_type == "event":
            print("1. Date")
            print("2. Duration")
            print("3. Description")
            print("4. ID")
            options = ["date", "duration", "description", "id"]

            criteria = input("Please enter the attribute you want to search(type 'exit' to go back): ")
            if criteria == "exit": return "exit"
            while not criteria.isdigit() or (criteria.isdigit() and (int(criteria) < 1 or int(criteria) > 4)):
                criteria = input(
                    "The option must be an integer between 1 and 3. Please enter again(type 'exit' to go back): ")
                if criteria == "exit": return "exit"

            return options[int(criteria) - 1]

    def search_person(self):
        """
        Searches a person
        :return: None
        """
        print("You selected to search for a person")

        criteria = self.get_criteria("person")
        if criteria == "exit":
            return
        input_search = input("Enter the person you want to search: ")

        condition, search_result = self.get_person_service().get_repository().search_by_criteria(criteria, input_search)

        if not search_result:
            print("No person found with the criteria and the search input entered")
        else:
            print(f"The search result for the input {input_search}")
            for person in search_result:
                print(person)
        while criteria != "exit":
            criteria = self.get_criteria("person")
            if criteria == "exit":
                return
            input_search = input("Enter the person you want to search: ")

            condition, search_result = self.get_person_service().get_repository().search_by_criteria(criteria, input_search)

            if not search_result:
                print("No person found with the criteria and the search input entered")
            else:
                print(f"The search result for the input {input_search}")
                for person in search_result:
                    print(person)

    def search_event(self):
        """
        Searches an event
        :return: None
        """
        print("You selected to search for an event")

        criteria = self.get_criteria("event")
        if criteria == "exit":
            return
        input_search = input("Enter the event you want to search: ")

        condition, search_result = self.get_event_service().get_repository().search_by_criteria(criteria, input_search)

        if not search_result:
            print("No event found with the criteria and the search input entered")
        else:
            print(f"The search result for the input {input_search}")
            for event in search_result:
                print(event)
        while criteria != "exit":
            criteria = self.get_criteria("event")
            if criteria == "exit":
                return
            input_search = input("Enter the event you want to search: ")

            condition, search_result = self.get_event_service().get_repository().search_by_criteria(criteria, input_search)

            if not search_result:
                print("No event found with the criteria and the search input entered")
            else:
                print(f"The search result for the input {input_search}")
                for event in search_result:
                    print(event)

    def search(self):
        """
        The method that implements the search functionality
        :return: None
        """
        print("You selected option 4: searching a person or an event")
        exit_app = input("If you want to go back to the main menu, type 'exit', else press Enter: ")
        if exit_app == "exit":
            return
        while True:
            print("You can search: ")
            print("1. A person")
            print("2. An event")
            option = input("Please enter the option you want to search(type 'exit' to return to the main menu): ")
            if option == "exit":
                return
            while not option.isdigit() or (option.isdigit() and (int(option) < 1 or int(option) > 2)):
                option = input(
                    "The option must be an integer between 1 and 2(or 'exit' to return to the main menu). Please enter again: ")
                if option == "exit":
                    return

            if option == "1":
                self.search_person()
            elif option == "2":
                self.search_event()

    def subscribe(self):
        """
        The method that implements the subscribe person to event functionality
        :return: None
        """
        print("You selected option 5: subscribe a person to an event")
        exit_app = input("If you want to go back to the main menu, type 'exit', else press Enter: ")
        if exit_app == 'exit':
            return
        print("\nThose are the current persons: ")
        self.get_person_service().get_repository().display()

        person_id = input(
            "\nPlease enter the id of the person you want to subscribe(enter 'exit' to go back to the main menu): ")
        if person_id == "exit": return
        while self.get_person_service().get_repository().get_element(person_id) is None:
            person_id = input("The id doesn't exist. Please enter again: ")
            if person_id == "exit": return

        selected_person = self.get_person_service().get_repository().get_element(person_id)
        print("\nThe person selected is:")
        print(selected_person)

        print("\nThe events available are: ")
        self.get_event_service().get_repository().display()

        event_id = input(
            "\nPlease enter the id of the event you want to subscribe the selected person(enter 'exit' to go back to the main menu): ")
        if event_id == "exit": return
        while (
                self.get_event_service().get_repository().get_element(event_id) is None or
                (self.get_event_service().get_repository().get_element(event_id)
                 and self.get_event_service().get_repository().get_element(event_id).exists(person_id)
                )
        ):
            event_id = input(
                "The id doesn't exist or the person is already subscribed in the event selected. Please enter again: ")
            if event_id == "exit": return

        selected_event = self.get_event_service().get_repository().get_element(event_id)
        print("\nThe selected event is:")
        print(selected_event)

        confirmation = input("\nDo you want to finish the subscribe process?(Yes/No): ")
        if confirmation.lower() == "yes":
            selected_person.add_event(selected_event)
            selected_event.add_person(selected_person)
            print("\nPerson subscribed successfully!")
        else:
            print("\nProcess terminated")

    def generate_sorted_list(self):
        """
        Generates a sorted list of the events a person is subscribed to based on a criteria
        :return: None
        """
        print("You selected to generate a sorted list with the events a specific person is attending to")
        print("You can sort by:")
        print("1. Description")
        print("2. Date")

        option = input("Please enter the option corresponding to the criteria you want to sort by: ")
        while not option.isdigit() or (option.isdigit() and (int(option) < 1 or int(option) > 2)):
            option = input("The option must be an integer between 1 and 2. Please enter again: ")

        person_id = input("Please enter the id of the person you want to generate the report: ")
        while self.get_person_service().get_repository().get_element(person_id) is None:
            person_id = input("The id doesn't exist. Please enter again: ")

        selected_person = self.get_person_service().get_repository().get_element(person_id)

        print(selected_person)

        sorted_list = []

        if option == "1":
            sorted_list = self.get_person_service().sort_by(selected_person.get_events(), lambda x: x.get_description())
        elif option == "2":
            sorted_list = self.get_person_service().sort_by(selected_person.get_events(),lambda x: tuple(map(int, x.get_date().split("/"))))

        criteria = "description" if option == 1 else "date"
        print(f"The sorted list based on the {criteria} is: ")
        for event in sorted_list:
            print(event)

    def calculate_max_events(self):
        """
        Prints the person that is subscribed to the most events
        :return: None
        """
        max_persons = self.get_person_service().calculate()
        is_list = isinstance(max_persons, list)
        print(f"The person{'s' if is_list else ''} that participate to the most events {'are' if is_list else 'is'}: ")
        if is_list:
            for person in max_persons: print(person)
        else:
            print(max_persons)

    def get_top_20(self):
        """
        Prints the top 20% of the events with the most subscribed persons
        :return: None
        """
        print("The top 20% of the events that have the most participants are: ")
        top_20_list = self.get_event_service().get_top_20_events()
        for event in top_20_list:
            print(event)

    def get_no_participants(self):
        if not self.get_event_service().get_repository().get_elements():
            print("There are no events available")

        print("The events with no participants are: ")
        result = self.get_event_service().get_no_participants()
        for event in result:
            print(event)

    def generate_reports(self):
        """
        The method that implements the generate reports functionality
        :return: None
        """
        print("You selected option 6: Generating reports")

        exit = input("If you want to go back to the main menu, type 'exit', otherwise press Enter: ")
        if exit.lower() == "exit":
            return

        print("You can generate 4 reports:")
        print("1. Sorted list with the events a specific person is attending to")
        print("2. The persons that joined the most events")
        print("3. The first 20% of the events with the most participants")
        print("4. Print the events without participants")

        option = input("Please enter the option you want to select: ")
        while not option.isdigit() or (option.isdigit() and (int(option) < 1 or int(option) > 4)):
            option = input("The option must be an integer between 1 and 3. Please enter again: ")

        if option == "1":
            self.generate_sorted_list()
        elif option == "2":
            self.calculate_max_events()
        elif option == "3":
            self.get_top_20()
        elif option == "4":
            self.get_no_participants()

    def get_person(self):
        """
        Prints a person based on the id given by the user
        :return: None
        """
        if not self.get_person_service().get_repository().get_elements():
            print("No persons available")
            return
        person_id = input("Please enter the id of the person you want to search(type 'exit' to go back): ")
        if person_id == "exit": return
        while self.get_person_service().get_repository().get_element(person_id) is None:
            person_id = input("The id doesn't exist. Please enter again(or 'exit' to go back): ")
            if person_id == "exit": return

        print(f"The person with the ID {person_id} is:")
        print(self.get_person_service().get_repository().get_element(person_id) )

    def get_event(self):
        """
        Prints an event based on the id given by the user
        :return: None
        """
        if not self.get_event_service().get_repository().get_elements():
            print("No events available")
            return
        event_id = input("Please enter the id of the event you want to search(type 'exit' to go back): ")
        if event_id == "exit": return
        while self.get_event_service().get_repository().get_element(event_id) is None:
            event_id = input("The id doesn't exist. Please enter again(or 'exit' to go back): ")
            if event_id == "exit": return

        print(f"The event with the ID {event_id} is:")
        print(self.get_event_service().get_repository().get_element(event_id))

    def get_info(self):
        """
        The method that lets the user identify an unique element
        :return: None
        """
        print("You can get the following info:")
        print("1. A person data")
        print("2. An event data")
        option = input("Please enter the option you want to get the info from: ")
        while not option.isdigit() or (option.isdigit() and (int(option) not in [1, 2])):
            option = input("The option must be an integer between 1 and 2. Please enter again: ")

        if option == "1":
            self.get_person()
        elif option == "2":
            self.get_event()

    def get_list(self):
        print("You can get the list for:")
        print("1. Persons")
        print("2. Events")
        option = input("Please enter the entity you want to get the list of: ")
        while option not in ["1", "2"]:
            option = input("The option must be an integer between 1 and 2. Please enter again: ")

        selected_list = self.get_person_service().get_repository().get_elements() if option == "1" else self.get_event_service().get_repository().get_elements()

        for element in selected_list:
            print(element)

    def generate_lists(self, number_of_instances):
        """
        Generates number_of_instances persons and number_of_instances // 2 event and random relation between the persons and the events
        :param number_of_instances: int
        :return: None
        """
        for i in range(number_of_instances):
            new_person = Person(str(i), f"name{i} surname{i}", f"address{i}")
            self.get_person_service().add(new_person)
            if i <= number_of_instances // 2:
                new_event = Event(str(100 * i), self.get_person_service().generate_rand_date(), 180 + i, f"description{i}")
                self.get_event_service().add(new_event)

        for i in range(number_of_instances):
            random_person_index = random.randrange(0, number_of_instances - 1)
            random_event_index = random.randrange(0, number_of_instances // 2)
            rand_person = self.get_person_service().get_repository().get_elements()[random_person_index]
            rand_event = self.get_event_service().get_repository().get_elements()[random_event_index]
            if not rand_event.exists(rand_person.get_id()):
                rand_person.add_event(rand_event)
                rand_event.add_person(rand_person)

    def generate_data(self):
        """
        The method that generates random data
        :return: None
        """
        number_of_instances = input("Enter the number of the elements you want to generate: ")

        while not number_of_instances.isdigit():
            number_of_instances = input("The number of elements must be a positive integer. Please enter again: ")

        number_of_instances = int(number_of_instances)
        self.generate_lists(number_of_instances)

        print("Data generated successfully!")


    def display_state(self):
        """
        Method that displays the current state of the application
        :return: None
        """
        print("The current app state is:")
        print(self.get_person_service().get_repository().get_elements())
        print(self.get_event_service().get_repository().get_elements())

    @staticmethod
    def exit_app():
        """
        Method that exits the app
        :return: None
        """
        print("----------------------------------")
        print("            App closed            ")
        print("----------------------------------")
        exit()

    def render_ui(self):
        """
        The method that renders the UI
        :return: None
        """

        menu = [(self.add, "Add a person or an event"),
            (self.modify, "Modify a person or an event"),
            (self.delete, "Delete a person or an event"),
            (self.search, "Search a person or an event"),
            (self.subscribe, "Subscribe a person to an event"),
            (self.generate_reports, "Get reports"),
            (self.get_info, "Get info"),
            (self.get_list, "Get list"),
            (self.generate_data, "Generate data"),
            (self.display_state, "Get current app state"),
            (self.exit_app, "Exit app")]

        print("------------------------------------")
        print("Welcome to the event manager system!")
        print("------------------------------------")


        while True:
            for index, i in enumerate(menu):
                print(f"Option {index + 1}. {i[1]}")

            option = input(f"Please select an option from 1 to {len(menu)}: ")
            while not option.isdigit() or (option.isdigit() and (int(option) < 1 or int(option) > len(menu))):
                option = input(
                    f"The option must be an integer between 1 and {len(menu)}. Please enter again the option: ")

            option = int(option)

            print()
            menu[option - 1][0]()
            print()