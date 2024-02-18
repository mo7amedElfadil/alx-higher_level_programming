#!/usr/bin/python3
"""Module to update a state to the database hbtn_0e_6_usa
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


def update_record(session, Table, id, name):
    """update record in the database
    """
    # update(Table).where(Table.id == id).values(name=name)
    update_record = session.query(Table).filter(Table.id == id).first()
    if update_record:
        update_record.name = name
        session.commit()

    # Commit the new state to the database


if __name__ == "__main__":
    # Create a new Engine
    engine = my_engine()
    Base.metadata.create_all(engine)
    # Generate new Session objects
    session = sessionmaker(bind=engine)()
    # Query the database
    if len(argv) == 4:
        update_record(session, State, 2, "New Mexico")
    else:
        update_record(session, State, argv[4], argv[5])
