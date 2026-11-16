from Domain.person_list import PersonList

class Event:
    """
    The class for the event entity with the following attributes:
        event_id: str
        date: str
        duration: int
        description: str
        subscribed_person: list[Person]
    """
    def __init__(self,event_id, date, duration, description):
        self.__event_id = event_id
        self.__date = date
        self.__duration = duration
        self.__description = description
        self.__subscribed_persons = []

    def get_event_id(self):
        return self.__event_id

    def get_date(self):
        return self.__date

    def set_date(self, new_date):
        self.__date = new_date

    def get_duration(self):
        return self.__duration

    def set_duration(self, new_duration):
        self.__duration = new_duration

    def get_description(self):
        return self.__description

    def set_description(self, new_description):
        self.__description = new_description

    def get_subscribed_persons(self):
        return self.__subscribed_persons

    def __str__(self):
        return f"""
    Event with the ID {self.get_event_id()}:
        Date: {self.get_date()}
        Duration: {self.get_duration()}
        Description: {self.get_description()}
        Subscribed persons: {self.get_subscribed_persons() if self.get_subscribed_persons() else "None"}
    """

    def __repr__(self):
        return f"Event with ID {self.get_event_id()}, date {self.get_date()}, duration {self.get_duration()}, description {self.get_description()}"

    def add_person(self, person):
        self.get_subscribed_persons().append(person)

    def exists(self, person_id):
        for person in self.get_subscribed_persons():
            if person.get_person_id() == person_id:
                return True

        return False