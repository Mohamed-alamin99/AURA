"""Knowledge base SQLAlchemy database model."""

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.infrastructure.database.base import Base


class KnowledgeBase(Base):
    __tablename__ = "knowledge_bases"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )

    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    owner_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False,
    )

    owner: Mapped["User"] = relationship(
        back_populates="knowledge_bases"
    )

    documents: Mapped[list["Document"]] = relationship(
        back_populates="knowledge_base"
    )
