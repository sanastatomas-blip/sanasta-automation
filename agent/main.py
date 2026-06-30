from gmail_reader import get_unread_emails
from invoice_parser import extract_invoice_data
from task_model import SanastaTask
from task_prioritizer import assign_priority, validate_task
from daily_board import build_daily_board, print_daily_board


def invoice_email_to_task(email):
    data = extract_invoice_data(email)
    task = SanastaTask(
        object_or_client=data.get("tiekejas") or "Nežinomas tiekėjas / sąskaita",
        value_eur=data.get("suma"),
        deadline=data.get("data"),
        responsible_person="Tomas",
        next_action="Patikrinti sąskaitą ir nuspręsti: apmokėti, ginčyti arba įtraukti į skolų kontrolę",
        recorded_in="Gmail",
        source="Gmail",
        notes=f"Failas: {data.get('failas')}",
        task_type="money",
    )
    return assign_priority(task)


def sample_tasks():
    """Temporary demo data until Gmail / CRM integrations are connected."""
    raw_tasks = [
        SanastaTask(
            object_or_client="Klientas laukia pasiūlymo dėl ŠVOK darbų",
            value_eur=900.0,
            deadline="2026-06-30",
            responsible_person="Tomas",
            next_action="Išsiųsti pasiūlymą ir suplanuoti follow-up",
            recorded_in="Gmail / CRM",
            source="manual",
            notes="Pinigai pirmiau už gražias idėjas",
        ),
        SanastaTask(
            object_or_client="SANASTA Quick Control CRM v1",
            deadline="2026-07-01",
            responsible_person="Tomas",
            next_action="Sutvarkyti laukus: Klientas, Telefonas, Task, Veiksmo data, Suma",
            recorded_in="CRM",
            source="manual",
            notes="Sistema, kad vadovas nebūtų vaikščiojantis serveris",
        ),
        SanastaTask(
            object_or_client="Senas neuždarytas laiškas",
            deadline="2026-06-30",
            responsible_person="Tomas",
            next_action="Priimti sprendimą: atsakyti, archyvuoti arba deleguoti",
            recorded_in="Gmail",
            source="manual",
            notes="Uždarymo disciplina",
        ),
    ]
    return [assign_priority(task) for task in raw_tasks]


def run():
    tasks = []

    emails = get_unread_emails()
    for email in emails:
        task = invoice_email_to_task(email)
        errors = validate_task(task)
        if errors:
            print(f"Užduotis turi klaidų: {errors}")
        tasks.append(task)

    if not tasks:
        tasks = sample_tasks()

    board = build_daily_board(tasks)
    print_daily_board(board)


if __name__ == "__main__":
    run()
