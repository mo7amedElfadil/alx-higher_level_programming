#!/usr/bin/python3
""" Module 100-relationship_states_cities.py
Creates the State “California” with the City “San Francisco”
from the database hbtn_0e_100_usa
"""
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


def create_states_cities(usr, pwd, db):
    """ Creates the State “California” with the City “San Francisco”
    from the database hbtn_0e_100_usa
    """
    # Create a new Engine instance.
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(usr, pwd, db), pool_pre_ping=True)
    # Create all tables in the database (if they don't exist).
    Base.metadata.create_all(engine)
    # Create a new session.
    session = sessionmaker(bind=engine)()
    # Create a new State and append a city to it
    new_state = State(name="California", cities=[City(name="San Francisco")])
    # Add the new State to the session.
    session.add(new_state)
    session.commit()
    session.close()


if __name__ == "__main__":
    if len(argv) == 4:
        create_states_cities(argv[1], argv[2], argv[3])
