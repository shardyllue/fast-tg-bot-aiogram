from typing import Any
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import Column, DateTime, BigInteger
from datetime import datetime


Base = declarative_base()


class UserTable(Base):
    __tablename__ = "user" 

    id = Column(BigInteger, primary_key=True)
    chat_id = Column(BigInteger, unique=True)
    registered_data = Column(DateTime, default=datetime.now())


    def __init__(
        self, chat_id : int
    ) -> None:
        self.chat_id = chat_id

