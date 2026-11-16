from Domain.person import Person

class PersonList:
    """
    The class for the person list entity with the following attributes:
        person_list: List[Person]
        person_history: List[List[Person]]
    """
    def __init__(self):
        self.__person_list = {
            "person_list": [],
            "person_history": []
        }

    def get_person_list(self):
        return self.__person_list["person_list"]

    def get_person_list_history(self):
        return self.__person_list["person_history"]

    def __str__(self):
        return f"""The current persons list state is:
        List: {self.get_person_list()}
        History: {self.get_person_list_history()}
    """

    def add_person(self, new_person):
        self.get_person_list().append(new_person)

    def delete(self, person_id):
        del_index = -1
        for index, person in enumerate(self.get_person_list()):
            if person.person_id == person_id:
                del_index = index

        self.get_person_list().pop(del_index)

    def get_entity(self, person_id):
        for person in self.get_person_list():
            if person.get_person_id() == person_id:
                return person

        return None



    def set_person_list(self, new_person_list):
        self.__person_list["person_list"] = new_person_list.copy()

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
            self.get_person_list()[index].add_event(event)

        return condition

    def display(self):
        for person in self.get_person_list():
            print(person)