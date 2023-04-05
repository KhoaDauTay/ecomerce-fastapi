from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.base_class import Base
from src.database.models import RoleModel


class UserModel(Base):
    username: Mapped[str] = mapped_column(
        String(length=20), unique=True
    )
    email: Mapped[str] = mapped_column(
        String(length=20), unique=True
    )
    full_name: Mapped[str] = mapped_column(
        String(length=30), unique=True
    )
    password: Mapped[str] = mapped_column(
        String(length=20)
    )
    role_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("role.id")
    )
    role: Mapped["RoleModel"] = relationship(
        "RoleModel", lazy="subquery"
    )
    list_address: Mapped[list["AddressModel"]] = relationship(
        back_populates="user"
    )

