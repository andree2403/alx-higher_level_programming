#!/usr/bin/python3
"""
This script prints the first State object
from the database `hbtn_0e_6_usa`.
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Access to the database and get a state
    from the database.
    """

    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    engine = create_engine(db_and)
    Session = sessionmaker(bind=engine)

    session = Session()
    i = session.query(State).order_by(State.id).first()
    if i is None:
        print('Nothing')
    else:
        print('{0}: {1}'.format(i.id, i.name))
