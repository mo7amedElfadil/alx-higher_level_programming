#!/usr/bin/python3
"""Module to fetch all cities from the database hbtn_0e_6_usa
"""
from re import T
from model_city import State, Base, City
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


def query_all(session, City, State):
    """Fetch all cities objects from the database
    """
    # Query the database
    return session.query(State.name, City.id, City.name)\
        .join(City, City.state_id == State.id).order_by(City.id).all()


if __name__ == "__main__":
    # Create a new Engine
    engine = my_engine()

    Base.metadata.create_all(engine)
    # Generate new Session objects
    session = sessionmaker(bind=engine)()
    # Query the database
    cities = query_all(session, City, State)
    for state, id, city in cities:
        print(f"{state}: ({id}) {city}")
