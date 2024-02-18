#!/usr/bin/python3
""" Module 101-relationship_states_cities_list.py
"""
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


def list_states_cities(usr, pwd, db):
    """ List all the State objects and the corresponding Cities
    from the database hbtn_0e_101_usa
    """
    # Create a new Engine instance.
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(usr, pwd, db), pool_pre_ping=True)
    # Create all tables in the database (if they don't exist).
    Base.metadata.create_all(engine)
    # Create a new session.
    session = sessionmaker(bind=engine)()
    query = session.query(State).order_by(State.id).all()
    for state in query:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("\t{}: {}".format(city.id, city.name))
    session.close()


if __name__ == "__main__":
    if len(argv) == 4:
        list_states_cities(argv[1], argv[2], argv[3])
