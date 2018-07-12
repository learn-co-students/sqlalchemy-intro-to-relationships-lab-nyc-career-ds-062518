from models import *
from sqlalchemy import create_engine

engine = create_engine('sqlite:///actors.db')

Session = sessionmaker(bind=engine)
session = Session()


def return_gwyneth_paltrows_roles():
    return [actor.roles for actor in session.query(Actor).filter_by(name = 'Gwyneth Paltrow').all()][0]

def return_tom_hanks_2nd_role():
    return [actor.roles for actor in session.query(Actor).filter_by(name = 'Tom Hanks').all()][0][1]
