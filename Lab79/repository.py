from Domain.person import Person
from Domain.event import Event

class Repository:
    """
    The class that implements the Repository
    """
    def __init__(self):
        self.__elements = []
        self.__history = []

    def update_history(self):
        """
        Updating the history when a change is made
        :return: None
        """
        self.__history.append(self.__elements.copy())

    def add(self, new_element):
        """
        Adding a new element
        :param new_element: Person | Event
        :return: None
        """
        self.update_history()
        self.__elements.append(new_element)

    def delete(self, element_id):
        """
        Deleting an element
        :param element_id: str
        :return: None
        """
        del_index = -1
        for index, element in enumerate(self.get_elements()):
            if element.get_id() == element_id:
                del_index = index

        if del_index == -1: return
        self.get_elements().pop(del_index)

    def get_elements(self):
        return self.__elements

    def get_history(self):
        return self.__history

    def set_elements(self, new_elements):
        """
        Sets the __elements list to the new_elements
        :param new_elements: List[Person | Event]
        :return: None
        """
        self.update_history()
        self.__elements = new_elements.copy()

    def get_element(self,element_id):
        for element in self.get_elements():
            if element.get_id() == element_id:
                return element

        return None

    def exists_id(self, element_id):
        for index, element in enumerate(self.get_elements()):
            if element.get_id() == element_id:
                return True, index

        return False, -1

    def undo(self):
        if not self.get_elements():
            return False
        self.set_elements(self.get_history().pop().copy())
        return True

    def display(self):
        for element in self.get_elements():
            print(element)


class PersonRepository(Repository):
    def __init__(self):
        super().__init__()

    def set_attribute(self, element_id, attribute, value):
        condition, index = self.exists_id(element_id)
        if condition:
            element = self.get_element(element_id)
            if element is None:
                return False
            new_element = None
            match attribute:
                case "name":
                    new_element = Person(element.get_id(), value, element.get_address(), element.get_events())
                case "address":
                    new_element = Person(element.get_id(), element.get_name(), value, element.get_events())
                case _:
                    return False
            self.get_elements()[index] = new_element
            return True

        return False

    def search_by_criteria(self, criteria, input_search):
        result_search = []
        match criteria:
            case "name":
                for element in self.get_elements():
                    if input_search in element.get_name():
                        result_search.append(element)
            case "address":
                for element in self.get_elements():
                    if input_search in element.get_address():
                        result_search.append(element)
            case "id":
                for element in self.get_elements():
                    if input_search in element.get_id():
                        result_search.append(element)
            case _:
                return False, None

        return True, result_search

    def add_event(self, event, person_id):
        condition, index = self.exists_id(person_id)
        if condition:
            self.get_elements()[index].add_event(event)

        return condition


class EventRepository(Repository):
    def __init__(self):
        super().__init__()

    def set_attribute(self, element_id, attribute, value):
        condition, index = self.exists_id(element_id)
        if condition:
            event = self.get_element(element_id)
            new_event = None
            match attribute:
                case "date":
                    new_event = Event(event.get_id(), value, event.get_duration(), event.get_description(), event.get_subscribed_persons())
                case "duration":
                    new_event = Event(event.get_id(), event.get_date(), value, event.get_description(), event.get_subscribed_persons())
                case "description":
                    new_event = Event(event.get_id(), event.get_date(), event.get_duration(), value, event.get_subscribed_persons())
                case _:
                    return False

            self.get_elements()[index] = new_event
            return True
        else:
            return False

    def search_by_criteria(self, criteria, input_search):
        result_search = []
        match criteria:
            case "id":
                for event in self.get_elements():
                    if input_search in event.get_id():
                        result_search.append(event)
            case "date":
                for event in self.get_elements():
                    if input_search in event.get_date():
                        result_search.append(event)
            case "duration":
                for event in self.get_elements():
                    if int(input_search) == event.get_duration():
                        result_search.append(event)
            case "description":
                for event in self.get_elements():
                    if input_search in event.get_description():
                        result_search.append(event)
            case _:
                return False, None

        return True, result_search

    def add_event(self, event, person_id):
        condition, index = self.exists_id(person_id)
        if condition:
            self.get_elements()[index].add_event(event)

        return condition