#!/usr/bin/python3
"""Module for model_city.py"""
from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base


class City(Base):
    """City class
    Args:
        Base (declarative_base): Base class
    Attributes:
        __tablename__ (str): Name of the table
        id (int): id of the City
        name (str): name of the state
        state_id (int): id of the state
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
