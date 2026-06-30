from datetime import date, datetime, timedelta
from typing import Optional

from task_model import SanastaTask


SYSTEM_KEYWORDS = [
    "crm",
    "calendar",
    "kalendorius",
    "trello",
    "template",
    "šablonas",
    "procesas",
    "standartas",
    "automatizacija",
    "sistema",
]

RISK_KEYWORDS = [
    "skola",
    "pretenzija",
    "skundas",
    "garantija",
    "teisinė rizika",
    "teisminis",
    "terminas",
    "klientas laukia",
]

MONEY_KEYWORDS = [
    "pasiūlymas",
    "sąskaita",
    "apmokėjimas",
    "pardavimas",
    "follow-up",
    "klientas",
    "objektas",
]


def _parse_deadline(deadline: Optional[str]) -> Optional[date]:
    if not deadline:
        return None
    try:
        return datetime.fromisoformat(deadline).date()
    except ValueError:
        return None


def _contains_any(text: str, keywords: list[str]) -> bool:
    text = text.lower()
    return any(keyword in text for keyword in keywords)


def assign_priority(task: SanastaTask) -> SanastaTask:
    """Assign A/B/C priority using Starteris-Valdovas discipline."""
    combined = f"{task.object_or_client} {task.next_action} {task.notes} {task.risk or ''}"
    deadline_date = _parse_deadline(task.deadline)
    urgent_deadline = deadline_date is not None and deadline_date <= date.today() + timedelta(days=1)

    has_money_or_risk = bool(task.value_eur) or bool(task.risk) or _contains_any(combined, RISK_KEYWORDS + MONEY_KEYWORDS)
    has_minimum_a_data = has_money_or_risk and bool(task.deadline) and bool(task.next_action)

    if has_minimum_a_data and urgent_deadline:
        task.priority = "A"
    elif has_minimum_a_data and _contains_any(combined, RISK_KEYWORDS + MONEY_KEYWORDS):
        task.priority = "A"
    elif _contains_any(combined, SYSTEM_KEYWORDS):
        task.priority = "B"
    else:
        task.priority = "C"

    if task.priority == "A" and task.value_eur:
        task.task_type = "money"
    elif task.priority == "B":
        task.task_type = "system"
    else:
        task.task_type = "closing"

    return task


def validate_task(task: SanastaTask) -> list[str]:
    errors = []
    if not task.object_or_client:
        errors.append("Trūksta object_or_client")
    if not task.next_action:
        errors.append("Trūksta next_action")
    if task.priority == "A":
        if not (task.value_eur or task.risk):
            errors.append("A prioritetui reikia value_eur arba risk")
        if not task.deadline:
            errors.append("A prioritetui reikia deadline")
        if not task.next_action:
            errors.append("A prioritetui reikia next_action")
    return errors
