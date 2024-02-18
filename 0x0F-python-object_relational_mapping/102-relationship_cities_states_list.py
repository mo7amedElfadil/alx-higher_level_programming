#!/usr/bin/python3
""" Module 102-relationship_cities_states_list.py
Creates the State “California” with the City “San Francisco”
from the database hbtn_0e_100_usa
"""
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


def list_cities_state(usr, pwd, db):
    """ List all the city objects and the corresponding states
    from the database hbtn_0e_101_usa
    """
    # Create a new Engine instance.
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(usr, pwd, db), pool_pre_ping=True)
    # Create all tables in the database (if they don't exist).
    Base.metadata.create_all(engine)
    # Create a new session.
    session = sessionmaker(bind=engine)()
    query = session.query(City).order_by(City.id).all()
    for city in query:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))
    session.close()


if __name__ == "__main__":
    if len(argv) == 4:
        list_cities_state(argv[1], argv[2], argv[3])
