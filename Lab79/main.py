from Lab79.repository import PersonRepository, EventRepository
from Lab79.service import Service
from Lab79.tests import run_all
from Lab79.ui import UI

if __name__ == "__main__":
    run_all()

    person_repository = PersonRepository()
    event_repository = EventRepository()

    person_service = Service(person_repository)
    event_service = Service(event_repository)

    ui = UI(person_service, event_service)

    ui.render_ui()
