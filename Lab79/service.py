import random
from time import strftime, gmtime
import math

class Service:
    def __init__(self, repository):
        self.__repository = repository

    def get_repository(self):
        return self.__repository

    def add(self, new_element):
        self.get_repository().add(new_element)

    def modify(self, element_id, attribute, value):
        self.get_repository().set_attribute(element_id, attribute, value)

    def delete(self, element_id):
        self.get_repository().delete(element_id)

    def display(self):
        self.get_repository().display()

    @staticmethod
    def valid_date(input_date, other_date=None, finish_date=None):
        """
        Returns a tuple with a bool and a feedback, indicating the validness of the input_date
        :param input_date: str
        :param other_date: str | None
        :param finish_date: str | None
        :return: str
        """

        if not input_date or len(input_date.split("/")) != 3:
            return False, "match the pattern dd/mm/yyyy, where dd,mm and yyyy must be valid integers"

        input_day, input_month, input_year = input_date.split("/")
        current_day, current_month, current_year = strftime("%d/%m/%Y", gmtime()).split("/")

        if not input_day.isdigit() or not input_month.isdigit() or not input_year.isdigit() or len(
                input_day) != 2 or len(input_month) != 2 or len(input_year) != 4:
            return False, "match the pattern dd/mm/yyyy, where dd,mm and yyyy must be valid integers"

        input_day = int(input_day)
        input_month = int(input_month)
        input_year = int(input_year)

        current_day = int(current_day)
        current_month = int(current_month)
        current_year = int(current_year)

        if input_day > 31 or input_month > 13:
            return False, "match the pattern dd/mm/yyyy, where dd,mm and yyyy must be valid integers"

        if current_year > input_year:
            return False, "be after the current date"
        elif current_year == input_year:
            if current_month > input_month:
                return False, "be after the current date"
            elif current_month == input_month:
                if current_day > input_day:
                    return False, "be after the current date"

        return True, ""

    @staticmethod
    def get_id():
        current_day, current_month, current_year = strftime("%d/%m/%Y", gmtime()).split("/")
        current_hour, current_minutes, current_second = strftime("%H/%M/%S", gmtime()).split("/")
        return "".join([current_day, current_month, current_year, current_hour, current_minutes, current_second])

    @staticmethod
    def date(event):
        day, month, year = map(int, event.get_date().split("/"))
        return (year, month, day)

    @staticmethod
    def description(event):
        return event.get_description()

    def sort_by(self, event_list, criteria=None):
        return sorted(event_list, key=criteria)

    def calculate(self):
        max_events = -1
        max_persons = []
        for person in self.get_repository().get_elements():
            if len(person.get_events()) > max_events:
                max_events = len(person.get_events())
                max_persons = [person]
            elif len(person.get_events()) == max_events:
                max_persons.append(person)

        return max_persons[0] if len(max_persons) == 1 else max_persons

    def get_top_20_events(self):
        event_list = self.get_repository().get_elements()
        top_20 = (math.ceil(len(event_list) / 5))
        sorted_event_list = sorted(event_list, key=lambda x: len(x.get_subscribed_persons()))
        sorted_event_list.reverse()
        return sorted_event_list[:top_20]

    @staticmethod
    def generate_rand_date():
        rand_day = random.randrange(1, 31)
        rand_month = random.randrange(1, 12)
        rand_year = random.randrange(2026, 2035)
        return f"{rand_day}/{rand_month}/{rand_year}"

    def get_no_participants(self):
        events = self.get_repository().get_elements()
        result = []

        for event in events:
            if not event.get_subscribed_persons():
                result.append(event)

        return result