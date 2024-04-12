from sqlalchemy import ForeignKey, TIMESTAMP
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class User(DeclarativeBase):
    __tablename__ = 'users'
    user_id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(nullable=False)
    last_name: Mapped[str] = mapped_column(nullable=False)
    register_date: Mapped[str] = mapped_column(TIMESTAMP, default=True)

    def __repr__(self):
        return f"<User username={self.first_name}"


class Login(DeclarativeBase):
    __tablename__ = 'login'
    user_id: Mapped[int] = mapped_column(ForeignKey('users.user_id'), nullable=False)
    email: Mapped[str] = mapped_column(nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)

    def __repr__(self):
        return f"<Login email={self.email}, name={self.user_id}"
