class Person:
    def __init__(self, person_id, name, address):
        self.person_id = person_id
        self.name = name
        self.address = address
        self.events = []

    def __str__(self):
        return f"""
    Person with the ID {self.person_id}:
        Name: {self.name}
        Address: {self.address}
    """

    def get_person_id(self):
        return self.person_id

    def get_name(self):
        return self.name

    def get_address(self):
        return self.address

    def get_events(self):
        return self.events

    def set_name(self, new_name):
        self.name = new_name

    def set_address(self, new_address):
        self.address = new_address

    def add_event(self, event):
        self.events.append(event)

class PersonList:
    def __init__(self):
        self.person_list = {
            "person_list": [],
            "person_history": []
        }

    def __str__(self):
        return f"""The current persons list state is:
        List: {self.person_list["person_list"]}
        History: {self.person_list["person_history"]}
    """

    def add_person(self, new_person):
        self.person_list["person_list"].append(new_person)

    def delete(self, person_id):
        del_index = -1
        for index, person in enumerate(self.get_person_list()):
            if person.person_id == person_id:
                del_index = index

        self.person_list["person_list"].pop(del_index)

    def get_entity(self, person_id):
        for person in self.person_list["person_list"]:
            if person.person_id == person_id:
                return person

        return None

    def get_person_list(self):
        return self.person_list["person_list"]

    def get_person_list_history(self):
        return self.person_list["person_history"]

    def set_person_list(self, new_person_list):
        self.person_list["person_list"] = new_person_list.copy()

    def exists_id(self, person_id):
        for index, person in enumerate(self.get_person_list()):
            if person.get_person_id() == person_id:
                return True, index

        return False, -1

    def set_attribute(self, person_id, attribute, value):
        condition, index = self.exists_id(person_id)
        if condition:
            person = self.get_entity(person_id)
            if person is None:
                return False
            new_person = None
            match attribute:
                case "name":
                    new_person = Person(person.get_person_id(), value, person.get_address())
                case "address":
                    new_person = Person(person.get_person_id(), person.get_name(), value)
                case _:
                    return False
            self.person_list["person_list"][index] = new_person
            return True

        return False

    def search_by_criteria(self, criteria, input_search):
        print(criteria)
        print(input_search)
        result_search = []
        match criteria:
            case "name":
                for person in self.get_person_list():
                    print(person.get_name())
                    if input_search in person.get_name():
                        result_search.append(person)
            case "address":
                for person in self.get_person_list():
                    if input_search in person.get_address():
                        result_search.append(person)
            case "id":
                for person in self.get_person_list():
                    if input_search in person.get_person_id():
                        result_search.append(person)
            case _:
                return False, None

        return True, result_search

    def add_event(self, event, person_id):
        condition, index = self.exists_id(person_id)
        if condition:
            self.person_list["person_list"][index].add_event(event)

        return condition

    def display(self):
        for person in self.get_person_list():
            print(person)

