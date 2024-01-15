#!/usr/bin/python3
"""a script that lists all City objects from the database hbtn_0e_101_usa"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import (sessionmaker, relationship)


if __name__ == "__main__":
    # Connect to the database
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(engine)
    session = Session()
    try:
        states = session.query(State).order_by(State.id)
        for state in states:
            for city in state.cities:
                print(city.id, city.name, sep=": ", end="")
                print(" -> " + state.name)
    finally:
        session.close()
