from sqlalchemy import create_engine, Column, Integer, String, Numeric
from decimal import Decimal
from sqlalchemy.orm import sessionmaker, declarative_base
import os


DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///ragnaflet.db")
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()


class Character(Base):
    __tablename__ = "characters"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    job = Column(String)
    level = Column(Integer, default=1, nullable=False)
    exp = Column(Integer, default=0, nullable=False)
    hp = Column(Integer, default=50, nullable=False)
    current_map = Column(String, default="")
    zeny = Column(Numeric(10, 2), nullable=False, default=Decimal("0.00"))


def init_db():
    Base.metadata.create_all(engine)


# Local Postgresql Database: postgresql://postgres:Betelgeuse@localhost:5432/ragna_flet
