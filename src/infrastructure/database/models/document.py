from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.infrastructure.database.base import Base

if TYPE_CHECKING:
    from src.infrastructure.database.models.knowledge_base import KnowledgeBase


class Document(Base):
    __tablename__ = "documents"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )

    knowledge_base_id: Mapped[int] = mapped_column(
        ForeignKey("knowledge_bases.id"),
        nullable=False,
    )

    filename: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    status: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        default="pending",
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )

    knowledge_base: Mapped["KnowledgeBase"] = relationship(
        back_populates="documents"
    )