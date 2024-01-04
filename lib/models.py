#!/usr/bin/env python3

from sqlalchemy import (Column, String, Integer)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
Base = declarative_base()
engine = create_engine('sqlite:///dogs.db')
class Dog(Base):
    __tablename__ = 'dogs'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    breed = Column(String())

