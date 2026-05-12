from typing import Sequence

from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base, Session

DATABASE_URL = "postgresql://postgres:postgres@db:5432/postgres"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)


class ItemModel(BaseModel):
    id: int
    name: str


app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)


@app.post("/items")
def create_item(name: str, db: Session = Depends(get_db)) -> ItemModel:
    item = Item(name=name)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


@app.get("/items")
def get_items(db: Session = Depends(get_db)) -> Sequence[ItemModel]:
    return db.query(Item).all()
