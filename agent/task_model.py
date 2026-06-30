from dataclasses import dataclass, asdict
from typing import Optional, Dict, Any


@dataclass
class SanastaTask:
    object_or_client: str
    next_action: str
    deadline: Optional[str] = None
    responsible_person: Optional[str] = None
    value_eur: Optional[float] = None
    risk: Optional[str] = None
    recorded_in: Optional[str] = None
    status: str = "new"
    priority: str = "C"
    source: str = "manual"
    notes: str = ""
    task_type: str = "closing"  # money, system, closing

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)
