from dataclasses import dataclass
from uuid import UUID


@dataclass
class KnowledgeBase:
    id: UUID
    name: str
    description: str | None = None
