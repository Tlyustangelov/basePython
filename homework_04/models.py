"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""

import os

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base, declared_attr, relationship

PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql+asyncpg://ilyas:passwd!@localhost/postgres"


async_engine = create_async_engine(
    PG_CONN_URI,
    echo=True,
)

Session = sessionmaker(
    async_engine,
    expire_on_commit=False,
    class_=AsyncSession
)


class Base:
    @declared_attr
    def __tablename__(cls):
        return f"{cls.__name__.lower()}s"

    id = Column(Integer, primary_key=True)


Base = declarative_base(bind=async_engine, cls=Base)


class User(Base):
    name = Column(String(30), unique=True)
    username = Column(String(20), unique=True)
    email = Column(String(30), unique=True)

    posts = relationship("Post", back_populates="user")


class Post(Base):
    user_id = Column(Integer, ForeignKey("users.id"), unique=False)
    title = Column(String(100), unique=True)
    body = Column(String(250), unique=True)

    user = relationship("User", back_populates="posts")
