from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

from .clarify.tool import ask_user
from .search_services.tool import search_services
from .search_doctors.tool import search_doctors
from .check_availability.tool import check_availability
from .book_appointment.tool import book_appointment
from .cancel_appointment.tool import cancel_appointment
from .clinic_policy.tool import clinic_policy


# These names are part of the fixed evaluation contract. Keep built-in names
# unchanged in tools.yaml, this registry and the supplied datasets. Improve
# descriptions and compatible schemas. Register any team-built bonus tool in
# this registry and tools.yaml, then test it with team-authored cases.
TOOL_FUNCTIONS = {
    "clarify": ask_user,
    "search_services": search_services,
    "search_doctors": search_doctors,
    "check_availability": check_availability,
    "book_appointment": book_appointment,
    "cancel_appointment": cancel_appointment,
    "clinic_policy": clinic_policy,
}


def load_tool_declarations(path: Path) -> list[dict[str, Any]]:
    return yaml.safe_load(Path(path).read_text(encoding="utf-8"))["tools"]


def to_openai_tools(declarations: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return [{
        "type": "function",
        "function": {
            "name": item["name"],
            "description": item.get("description", ""),
            "parameters": item.get("parameters", {"type": "object", "properties": {}}),
        },
    } for item in declarations]
