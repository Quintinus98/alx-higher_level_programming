#!/usr/bin/python3
"""A script that prints all City objects from the database"""
import sys
from model_state import Base, State
from model_city import City
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
        states = session.query(State.name, City.id, City.name) \
                              .filter(State.id == City.state_id) \
                              .order_by(City.id)
        for row in states:
            print("{}: {} {}".format(row[0], row[1], row[2]))
    finally:
        session.close()
