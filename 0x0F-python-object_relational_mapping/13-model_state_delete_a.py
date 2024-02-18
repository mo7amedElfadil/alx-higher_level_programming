#!/usr/bin/python3
"""Module to delete all state objects with name containing letter a
from the database hbtn_0e_6_usa
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


def delete_record(session, Table, character='a'):
    """delete record in the database using the object from the session
    """
    # Query the database
    records = session.query(Table)\
        .filter(Table.name.like('%{}%'.format(character)))
    # Delete the records
    for record in records:
        session.delete(record)
    # Commit the changes
    session.commit()


if __name__ == "__main__":
    # Create a new Engine
    engine = my_engine()
    Base.metadata.create_all(engine)
    # Generate new Session objects
    session = sessionmaker(bind=engine)()
    # Query the database
    if len(argv) == 4:
        delete_record(session, State, 'a')
    else:
        delete_record(session, State, argv[4])
