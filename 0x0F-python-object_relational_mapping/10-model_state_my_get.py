#!/usr/bin/python3
"""Module to filter states from the database hbtn_0e_6_usa
"""
from model_state import Base, State

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


def my_engine():
    """Create a new instance of Engine
    """
    # Create a new Engine instance
    return create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                         .format(argv[1], argv[2], argv[3]),
                         pool_pre_ping=True)


def filter_query_first(session, Table, pattern):
    """Filter the database and get the first result
    """
    # Query the database
    # return session.query(Table).filter(Table.name == pattern).first()
    return session.query(Table).filter(Table.name == pattern).scalar()


if __name__ == "__main__":
    # Create a new Engine
    engine = my_engine()
    Base.metadata.create_all(engine)
    # Generate new Session objects
    session = sessionmaker(bind=engine)()
    # Query the database
    state = filter_query_first(session, State, argv[4])
    if not state:
        print("Not found")
    else:
        print(f"{state.id}")
