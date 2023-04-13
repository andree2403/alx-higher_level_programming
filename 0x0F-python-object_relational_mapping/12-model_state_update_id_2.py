#!/usr/bin/python3
"""
This script lists all State objects
from the database `hbtn_0e_6_usa`.
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Access to the database and get the states
    from the database.
    """

    db_dre = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    engine = create_engine(db_dre)
    Session = sessionmaker(bind=engine)

    session = Session()

    results = session.query(State).filter(State.id == '2')

    for i in results:
        i.name = "New Mexico"

    session.commit()
