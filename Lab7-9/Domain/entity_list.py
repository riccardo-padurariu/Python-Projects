from Domain.person_list import PersonList
from Domain.event_list import EventList

class EntityList:
    """
    The class for the entity list with the following attributes:
        person_list: PersonList
        event_list: EventList
    """
    def __init__(self):
        self.__person_list = PersonList()
        self.__event_list = EventList()

    def get_person_list(self):
        return self.__person_list

    def get_event_list(self):
        return self.__event_list

    def add_person(self, person):
        self.get_person_list().get_person_list().append(person)

    def add_event(self, event):
        self.get_event_list().get_event_list().append(event)

    def set_person_list(self, new_person_list):
        self.get_person_list().set_person_list(new_person_list)

    def set_event_list(self, new_event_list):
        self.get_event_list().set_event_list(new_event_list)

    def set_attribute(self, entity_type, entity_id, attribute, value):

        match entity_type:
            case "person":
                self.get_person_list().set_attribute(entity_id, attribute, value)
                return True
            case "event":
                self.get_event_list().set_attribute(entity_id, attribute, value)
                return True
            case _ :
                return False
