from Domain.person_domain import PersonList

class Event:
    def __init__(self,event_id, date, duration, description):
        self.event_id = event_id
        self.date = date
        self.duration = duration
        self.description = description
        self.subscribed_persons = []

    def __str__(self):
        return f"""
    Event with the ID {self.event_id}:
        Date: {self.date}
        Duration: {self.duration}
        Description: {self.description}
        Subscribed persons: {self.subscribed_persons if self.subscribed_persons else "None"}
    """

    def get_event_id(self):
        return self.event_id

    def get_date(self):
        return self.date

    def get_duration(self):
        return self.duration

    def get_description(self):
        return self.description

    def set_date(self, new_date):
        self.date = new_date

    def set_duration(self, new_duration):
        self.duration = new_duration

    def set_description(self, new_description):
        self.description = new_description

    def add_person(self, person):
        self.subscribed_persons.append(person)


class EventList:
    def __init__(self):
        self.event_list = {
            "event_list": [],
            "event_history": []
        }

    def __str__(self):
        return f"""The current persons list state is:
        List: {self.event_list["event_list"]}
        History: {self.event_list["event_history"]}
    """

    def get_event_list(self):
        return self.event_list["event_list"]

    def get_event_list_history(self):
        return self.event_list["event_history"]

    def add_event(self, event):
        self.event_list["event_list"].append(event)

    def delete(self, event_id):
        del_index = -1
        for index, event in enumerate(self.get_event_list()):
            if event.event_id == event_id:
                del_index = index

        self.event_list["event_list"].pop(del_index)

    def set_event_list(self, new_event_list):
        self.event_list["event_list"] = new_event_list.copy()

    def get_entity(self, event_id):
        for event in self.get_event_list():
            if event.event_id == event_id:
                return event

        return None

    def exists_id(self, event_id):
        for index, event in enumerate(self.get_event_list()):
            if event.event_id == event_id:
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

            self.event_list["event_list"][index] = new_event
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
            self.event_list["event_list"][index].add_person(person)

        return condition

    def display(self):
        for event in self.get_event_list():
            print(event)

class EntityList:
    def __init__(self):
        self.person_list = PersonList()
        self.event_list = EventList()

    def get_person_list(self):
        return self.person_list

    def get_event_list(self):
        return self.event_list

    def add_person(self, person):
        self.person_list.get_person_list().append(person)

    def add_event(self, event):
        self.event_list.get_event_list().append(event)

    def set_person_list(self, new_person_list):
        self.person_list.set_person_list(new_person_list)

    def set_event_list(self, new_event_list):
        self.event_list.set_event_list(new_event_list)

    def set_attribute(self, entity_type, entity_id, attribute, value):

        match entity_type:
            case "person":
                self.person_list.set_attribute(entity_id, attribute, value)
                return True
            case "event":
                self.event_list.set_attribute(entity_id, attribute, value)
                return True
            case _ :
                return False
