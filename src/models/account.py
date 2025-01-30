from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class AccountModelResponse(BaseModel):  # Modelo Pydantic para o fastapi
    name: str
    number: int

    class ConfigDict:
        from_attributes = True


class AccountModel(Base):  # Modelo sqlalchemy para a interacao com o db
    __tablename__ = "Accounts"

    id = Column(Integer, primary_key=True, autoincrement=True)
    Name = Column(String(30), nullable=False)
    Number = Column(Integer, nullable=False)

    def __repr__(self):
        return f"AccountModel(id={self.id!r}, name={self.Name!r}, number={self.Number!r})"
