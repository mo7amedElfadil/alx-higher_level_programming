#!/usr/bin/python3
"""Module to add a new state to the database hbtn_0e_6_usa
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


def insert_new_record(session, Table, name):
    """Insert a new record (state) to the database
    """
    # Create a new state
    new_state = Table(name=name)
    # Add the new state to the database
    session.add(new_state)
    # Commit the new state to the database
    session.commit()
    new_record = session.query(Table).filter_by(name=name).scalar()
    print(new_record.id)


if __name__ == "__main__":
    # Create a new Engine
    engine = my_engine()
    Base.metadata.create_all(engine)
    # Generate new Session objects
    session = sessionmaker(bind=engine)()
    # Query the database
    if len(argv) == 4:
        insert_new_record(session, State, "Louisiana")
    else:
        insert_new_record(session, State, argv[4])
