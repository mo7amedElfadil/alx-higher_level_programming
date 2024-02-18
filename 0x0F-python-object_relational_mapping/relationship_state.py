#!/usr/bin/python3
"""Module for relationship_state.py"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """State class
    Args:
        Base (declarative_base): Base class
    Attributes:
        __tablename__ (str): Name of the table
        id (int): id of the state
        name (str): name of the state
        cities (relationship): relationship with the City class
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    # set the relationship with the City class and cascade delete the cities
    # when the state is deleted
    cities = relationship("City", backref="state", cascade="all, delete-orphan")
