import math


def date(event):
    day, month, year = map(int, event.get_date().split("/"))
    return (year, month, day)

def description(event):
    return event.get_description()

def sort_by(person_list, criteria = None):
    print(person_list)
    return sorted(person_list, key=criteria)

def calculate(person_list):
    max_events = -1
    max_persons = []
    for person in person_list.get_person_list():
        if len(person.get_events()) > max_events:
            max_events = len(person.get_events())
            max_persons = [person]
        elif len(person.get_events()) == max_events:
            max_persons.append(person)

    return max_persons[0] if len(max_persons) == 1 else max_persons

def get_top_20_events(event_list):
    top_20 = math.ceil(len(event_list.get_event_list()) / 5)
    sorted_event_list = sorted(event_list.get_event_list(), key=lambda x: len(x.get_subscribed_persons()))
    sorted_event_list.reverse()
    return sorted_event_list[:top_20]