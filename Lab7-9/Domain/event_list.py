from Domain.event import Event

class EventList:
    """
    The class for the event list entity with the following attributes:
        event_list: List[Event]
        event_history: List[List[Event]]
    """
    def __init__(self):
        self.__event_list = {
            "event_list": [],
            "event_history": []
        }

    def get_event_list(self):
        return self.__event_list["event_list"]

    def get_event_list_history(self):
        return self.__event_list["event_history"]

    def __str__(self):
        return f"""The current persons list state is:
        List: {self.get_event_list()}
        History: {self.get_event_list_history()}
    """

    def add_event(self, event):
        self.get_event_list().append(event)

    def delete(self, event_id):
        del_index = -1
        for index, event in enumerate(self.get_event_list()):
            if event.event_id == event_id:
                del_index = index

        self.get_event_list().pop(del_index)

    def set_event_list(self, new_event_list):
        self.__event_list["event_list"] = new_event_list.copy()

    def get_entity(self, event_id):
        for event in self.get_event_list():
            if event.get_event_id() == event_id:
                return event

        return None

    def exists_id(self, event_id):
        for index, event in enumerate(self.get_event_list()):
            if event.get_event_id() == event_id:
                return True, index

        return False, -1

    def set_attribute(self, event_id, attribute, value):
        condition, index = self.exists_id(event_id)
        if condition:
            event = self.get_entity(event_id)
            new_event = None
            match attribute:
                case "date":
                    new_event = Event(event.get_event_id(), value, event.get_duration(), event.get_description())
                case "duration":
                    new_event = Event(event.get_event_id(), event.get_date(), value, event.get_description())
                case "description":
                    new_event = Event(event.get_event_id(), event.get_date(), event.get_duration, value)
                case _:
                    return False

            self.get_event_list()[index] = new_event
            return True
        else:
            return False

    def search_by_criteria(self, criteria, input_search):
        result_search = []
        match criteria:
            case "id":
                for event in self.get_event_list():
                    if input_search in event.get_event_id():
                        result_search.append(event)
            case "date":
                for event in self.get_event_list():
                    if input_search == event.get_date():
                        result_search.append(event)
            case "duration":
                for event in self.get_event_list():
                    if int(input_search) == event.get_duration():
                        result_search.append(event)
            case "description":
                for event in self.get_event_list():
                    if input_search in event.get_description():
                        result_search.append(event)
            case _:
                return False, None

        return True, result_search

    def add_person(self, person, event_id):
        condition, index = self.exists_id(event_id)
        if condition:
            self.get_event_list()[index].add_person(person)

        return condition

    def display(self):
        for event in self.get_event_list():
            print(event)