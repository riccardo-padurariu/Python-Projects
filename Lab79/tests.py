import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from Domain.person import Person
from Domain.event import Event
from repository import Repository, PersonRepository, EventRepository
from service import Service

def create_person(i=1):
    return Person(str(i), f"Name{i} Surname{i}", f"Address{i}")


def create_event(i=1, date="01/01/2099"):
    return Event(str(i), date, 60 + i, f"Description{i}")

def test_person_getters():
    p = Person("1", "Ana Pop", "Cluj")
    assert p.get_id() == "1"
    assert p.get_name() == "Ana Pop"
    assert p.get_address() == "Cluj"
    assert p.get_events() == []


def test_person_setters():
    p = create_person()
    p.set_name("New Name")
    p.set_address("New Address")
    assert p.get_name() == "New Name"
    assert p.get_address() == "New Address"


def test_person_add_event():
    p = create_person()
    e = create_event()
    p.add_event(e)
    assert p.get_events() == [e]


def test_person_str_and_repr():
    p = create_person()
    assert "Name1 Surname1" in str(p)
    assert "None" in str(p)
    assert "Address1" in repr(p)
    assert "ID 1" in repr(p)

def test_event_getters():
    e = Event("5", "10/10/2099", 90, "Party")
    assert e.get_id() == "5"
    assert e.get_date() == "10/10/2099"
    assert e.get_duration() == 90
    assert e.get_description() == "Party"
    assert e.get_subscribed_persons() == []


def test_event_setters():
    e = create_event()
    e.set_date("02/02/2099")
    e.set_duration(10)
    e.set_description("Changed")
    assert e.get_date() == "02/02/2099"
    assert e.get_duration() == 10
    assert e.get_description() == "Changed"


def test_event_add_person_and_exists():
    e = create_event()
    p = create_person()
    assert not e.exists(p.get_id())
    e.add_person(p)
    assert e.get_subscribed_persons() == [p]
    assert e.exists(p.get_id())
    assert not e.exists("999")


def test_event_str_and_repr():
    e = create_event()
    assert "Description1" in str(e)
    assert "None" in str(e)  # no subscribed persons yet
    assert "Description1" in repr(e)
    assert "ID 1" in repr(e)


def test_repository_add_and_get_elements():
    repo = Repository()
    assert repo.get_elements() == []
    p = create_person()
    repo.add(p)
    assert repo.get_elements() == [p]


def test_repository_get_element():
    repo = Repository()
    p1, p2 = create_person(1), create_person(2)
    repo.add(p1)
    repo.add(p2)
    assert repo.get_element("2") is p2
    assert repo.get_element("404") is None


def test_repository_exists_id():
    repo = Repository()
    repo.add(create_person(1))
    repo.add(create_person(2))
    assert repo.exists_id("2") == (True, 1)
    assert repo.exists_id("404") == (False, -1)


def test_repository_delete():
    repo = Repository()
    p1, p2 = create_person(1), create_person(2)
    repo.add(p1)
    repo.add(p2)
    repo.delete("1")
    assert repo.get_elements() == [p2]


def test_repository_delete_nonexistent_id_changes_nothing():
    repo = Repository()
    p1, p2 = create_person(1), create_person(2)
    repo.add(p1)
    repo.add(p2)
    repo.delete("404")
    assert repo.get_elements() == [p1, p2]


def test_repository_set_elements_copies_list():
    repo = Repository()
    source = [create_person(1), create_person(2)]
    repo.set_elements(source)
    source.append(create_person(3))
    assert len(repo.get_elements()) == 2


def test_repository_history_grows_on_add():
    repo = Repository()
    repo.add(create_person(1))
    repo.add(create_person(2))
    history = repo.get_history()
    assert len(history) == 2
    assert history[0] == []
    assert len(history[1]) == 1


def test_person_repo_set_name():
    repo = PersonRepository()
    repo.add(create_person(1))
    assert repo.set_attribute("1", "name", "Maria Ionescu") is True
    assert repo.get_element("1").get_name() == "Maria Ionescu"
    assert repo.get_element("1").get_address() == "Address1"


def test_person_repo_set_address():
    repo = PersonRepository()
    repo.add(create_person(1))
    assert repo.set_attribute("1", "address", "Oradea") is True
    assert repo.get_element("1").get_address() == "Oradea"
    assert repo.get_element("1").get_name() == "Name1 Surname1"


def test_person_repo_set_attribute_invalid_attribute_or_id():
    repo = PersonRepository()
    repo.add(create_person(1))
    assert repo.set_attribute("1", "age", 20) is False
    assert repo.set_attribute("404", "name", "X Y") is False


def test_person_repo_set_attribute_keeps_events():
    repo = PersonRepository()
    p = create_person(1)
    e = create_event(1)
    p.add_event(e)
    repo.add(p)
    repo.set_attribute("1", "name", "Maria Ionescu")
    assert repo.get_element("1").get_events() == [e]


def test_person_repo_search_by_name():
    repo = PersonRepository()
    repo.add(Person("1", "Ana Pop", "Cluj"))
    repo.add(Person("2", "Ion Popescu", "Brasov"))
    repo.add(Person("3", "Maria Ionescu", "Cluj"))
    ok, result = repo.search_by_criteria("name", "Pop")
    assert ok is True
    assert [p.get_id() for p in result] == ["1", "2"]


def test_person_repo_search_by_address():
    repo = PersonRepository()
    repo.add(Person("1", "Ana Pop", "Cluj"))
    repo.add(Person("2", "Ion Popescu", "Brasov"))
    ok, result = repo.search_by_criteria("address", "Cluj")
    assert ok is True
    assert [p.get_id() for p in result] == ["1"]


def test_person_repo_search_by_id():
    repo = PersonRepository()
    repo.add(Person("11", "Ana Pop", "Cluj"))
    repo.add(Person("22", "Ion Popescu", "Brasov"))
    ok, result = repo.search_by_criteria("id", "1")
    assert ok is True
    assert [p.get_id() for p in result] == ["11"]


def test_person_repo_search_no_match_and_invalid_criteria():
    repo = PersonRepository()
    repo.add(create_person(1))
    assert repo.search_by_criteria("name", "zzz") == (True, [])
    assert repo.search_by_criteria("age", "1") == (False, None)


def test_person_repo_add_event():
    repo = PersonRepository()
    repo.add(create_person(1))
    e = create_event(1)
    assert repo.add_event(e, "1") is True
    assert repo.get_element("1").get_events() == [e]
    assert repo.add_event(e, "404") is False


def test_event_repo_set_date():
    repo = EventRepository()
    repo.add(create_event(1))
    assert repo.set_attribute("1", "date", "05/05/2099") is True
    assert repo.get_element("1").get_date() == "05/05/2099"


def test_event_repo_set_duration():
    repo = EventRepository()
    repo.add(create_event(1))
    assert repo.set_attribute("1", "duration", 500) is True
    assert repo.get_element("1").get_duration() == 500


def test_event_repo_set_description():
    repo = EventRepository()
    repo.add(create_event(1))
    assert repo.set_attribute("1", "description", "Brand new") is True
    event = repo.get_element("1")
    assert event.get_description() == "Brand new"
    assert event.get_duration() == 61


def test_event_repo_set_attribute_invalid_attribute_or_id():
    repo = EventRepository()
    repo.add(create_event(1))
    assert repo.set_attribute("1", "location", "x") is False
    assert repo.set_attribute("404", "date", "05/05/2099") is False


def test_event_repo_set_attribute_keeps_subscribed_persons():
    repo = EventRepository()
    e = create_event(1)
    p = create_person(1)
    e.add_person(p)
    p.add_event(e)
    repo.add(e)
    repo.set_attribute("1", "date", "05/05/2099")
    assert repo.get_element("1").get_subscribed_persons() == [p]


def test_event_repo_search_by_description():
    repo = EventRepository()
    repo.add(Event("1", "01/01/2099", 60, "Birthday party"))
    repo.add(Event("2", "02/01/2099", 90, "Conference"))
    ok, result = repo.search_by_criteria("description", "party")
    assert ok is True
    assert [e.get_id() for e in result] == ["1"]


def test_event_repo_search_by_id_and_date():
    repo = EventRepository()
    repo.add(Event("11", "01/01/2099", 60, "A"))
    repo.add(Event("22", "02/01/2099", 90, "B"))
    ok, result = repo.search_by_criteria("id", "1")
    assert ok is True and [e.get_id() for e in result] == ["11"]
    ok, result = repo.search_by_criteria("date", "02/01")
    assert ok is True and [e.get_id() for e in result] == ["22"]


def test_event_repo_search_invalid_criteria():
    repo = EventRepository()
    repo.add(create_event(1))
    assert repo.search_by_criteria("nonsense", "x") == (False, None)


def test_service_get_repository():
    repo = PersonRepository()
    assert Service(repo).get_repository() is repo


def test_service_add_modify_delete():
    service = Service(PersonRepository())
    service.add(create_person(1))
    assert len(service.get_repository().get_elements()) == 1
    service.modify("1", "name", "Maria Ionescu")
    assert service.get_repository().get_element("1").get_name() == "Maria Ionescu"
    service.delete("1")
    assert service.get_repository().get_elements() == []


def test_valid_date_accepts_future_dates():
    assert Service.valid_date("01/01/2099") == (True, "")
    assert Service.valid_date("31/12/2099") == (True, "")


def test_valid_date_rejects_past_dates():
    ok, feedback = Service.valid_date("01/01/2000")
    assert ok is False
    assert "after the current date" in feedback


def test_valid_date_rejects_bad_format():
    for bad in ["", "1/1/2099", "01-01-2099", "01/01/99", "aa/bb/cccc", "01/01", "01/01/2099/1"]:
        ok, _ = Service.valid_date(bad)
        assert ok is False, f"{bad!r} should be invalid"

def test_get_id_format():
    new_id = Service.get_id()
    assert isinstance(new_id, str)
    assert len(new_id) == 14
    assert new_id.isdigit()


def test_service_date_key():
    event = Event("1", "25/12/2099", 60, "x")
    assert Service.date(event) == (2099, 12, 25)


def test_service_description_key():
    event = Event("1", "25/12/2099", 60, "Hello")
    assert Service.description(event) == "Hello"


def test_sort_by_description():
    service = Service(EventRepository())
    events = [Event("1", "01/01/2099", 1, "b"), Event("2", "01/01/2099", 1, "a"),
              Event("3", "01/01/2099", 1, "c")]
    result = service.sort_by(events, Service.description)
    assert [e.get_id() for e in result] == ["2", "1", "3"]
    assert [e.get_id() for e in events] == ["1", "2", "3"]


def test_sort_by_date_chronological():
    service = Service(EventRepository())
    events = [Event("1", "01/01/2100", 1, "x"), Event("2", "31/12/2099", 1, "x"),
              Event("3", "15/06/2099", 1, "x")]
    result = service.sort_by(events, Service.date)
    assert [e.get_id() for e in result] == ["3", "2", "1"]


def test_calculate_single_max_person():
    service = Service(PersonRepository())
    p1, p2 = create_person(1), create_person(2)
    p1.add_event(create_event(1))
    p1.add_event(create_event(2))
    p2.add_event(create_event(1))
    service.add(p1)
    service.add(p2)
    assert service.calculate() is p1


def test_calculate_tie_returns_list():
    service = Service(PersonRepository())
    p1, p2, p3 = create_person(1), create_person(2), create_person(3)
    p1.add_event(create_event(1))
    p2.add_event(create_event(1))
    service.add(p1)
    service.add(p2)
    service.add(p3)
    result = service.calculate()
    assert isinstance(result, list)
    assert result == [p1, p2]


def test_get_top_20_events():
    service = Service(EventRepository())
    events = [create_event(i) for i in range(10)]
    for i, event in enumerate(events):
        for j in range(i):
            event.add_person(create_person(j))
        service.add(event)
    top = service.get_top_20_events()
    assert [e.get_id() for e in top] == ["9", "8"]


def test_get_top_20_events_rounds_up():
    service = Service(EventRepository())
    service.add(create_event(1))
    assert len(service.get_top_20_events()) == 1
    assert Service(EventRepository()).get_top_20_events() == []


def test_generate_rand_date_shape():
    for _ in range(50):
        date = Service.generate_rand_date()
        day, month, year = map(int, date.split("/"))
        assert 1 <= day <= 31
        assert 1 <= month <= 12
        assert 2026 <= year <= 2035


def run_all():
    tests = [(name, fn) for name, fn in sorted(globals().items())
             if name.startswith("test_") and callable(fn)]
    failed = []
    for name, fn in tests:
        fn()

    print(f"\n{len(tests) - len(failed)}/{len(tests)} tests passed")
    return not failed