from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class AccountModelResponse(BaseModel):
    name: str
    number: int

    class Config:
        from_attributes = True


class AccountModel(Base):
    __tablename__ = "Accounts"

    id = Column(Integer, primary_key=True, autoincrement=True)
    Name = Column(String(30), nullable=False)
    Number = Column(Integer, nullable=False)

    def __repr__(self):
        return f"AccountModel(id={self.id!r}, name={self.Name!r}, number={self.Number!r})"
