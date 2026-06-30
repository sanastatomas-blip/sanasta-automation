from typing import Iterable, Dict, List

from task_model import SanastaTask


def build_daily_board(tasks: Iterable[SanastaTask]) -> Dict[str, List[dict]]:
    """Return only the daily 3 closures: money, system, closing."""
    buckets = {
        "money_action": [],
        "system_action": [],
        "closing_action": [],
    }

    sorted_tasks = sorted(tasks, key=lambda task: {"A": 0, "B": 1, "C": 2}.get(task.priority, 3))

    for task in sorted_tasks:
        if task.task_type == "money" and not buckets["money_action"]:
            buckets["money_action"].append(task.to_dict())
        elif task.task_type == "system" and not buckets["system_action"]:
            buckets["system_action"].append(task.to_dict())
        elif task.task_type == "closing" and not buckets["closing_action"]:
            buckets["closing_action"].append(task.to_dict())

    return buckets


def print_daily_board(board: Dict[str, List[dict]]) -> None:
    print("\nSANASTA šiandienos 3 uždarymai")
    print("--------------------------------")
    labels = {
        "money_action": "1. Pinigų veiksmas",
        "system_action": "2. Sistemos veiksmas",
        "closing_action": "3. Uždarymo veiksmas",
    }

    for key, label in labels.items():
        items = board.get(key, [])
        if not items:
            print(f"{label}: nėra")
            continue
        task = items[0]
        print(f"{label}: {task['object_or_client']} -> {task['next_action']} [{task['priority']}]")
