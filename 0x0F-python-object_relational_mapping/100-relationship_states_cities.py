#!/usr/bin/python3
"""A script that lists all State objects from the database
hbtn_0e_6_usa"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # Connect to the database
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(engine)
    session = Session()
    try:
        newState = State(name='California')
        newCity = City(name='San Francisco')
        newState.cities.append(newCity)
        session.add(newState)
        session.add(newCity)
        session.commit()
    finally:
        session.close()
