from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.infrastructure.database.base import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )

    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False,
    )

    knowledge_bases: Mapped[list["KnowledgeBase"]] = relationship(
        back_populates="owner"
    )
