class Person:
    """
    The person class for the person entity with the following attributes:
        person_id: str
        name: str
        address: str
        events: List[Event]
    """
    def __init__(self, person_id, name, address, events = None):
        self.__person_id = person_id
        self.__name = name
        self.__address = address
        self.__events = [] if not events else events

    def get_id(self):
        return self.__person_id

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name

    def get_address(self):
        return self.__address

    def set_address(self, new_address):
        self.__address = new_address

    def get_events(self):
        return self.__events

    def __str__(self):
        return f"""
    Person with the ID {self.get_id()}:
        Name: {self.get_name()}
        Address: {self.get_address()}
        Events: {self.get_events() if self.get_events() else "None"}
    """

    def __repr__(self):
        return f"Person with ID {self.get_id()}, name {self.get_name()}, address {self.get_address()}"

    def add_event(self, event):
        self.get_events().append(event)

