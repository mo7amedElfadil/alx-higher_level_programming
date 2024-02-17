#!/usr/bin/python3
"""Module for model_state.py"""
from sqlalchemy import Column, Integer, String
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
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

