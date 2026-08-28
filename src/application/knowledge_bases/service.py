from uuid import uuid4

from src.domain.knowledge_bases.models import KnowledgeBase


class KnowledgeBaseService:

    def create(
        self,
        name: str,
        description: str | None = None,
    ) -> KnowledgeBase:

        knowledge_base = KnowledgeBase(
            id=uuid4(),
            name=name,
            description=description,
        )

        return knowledge_base