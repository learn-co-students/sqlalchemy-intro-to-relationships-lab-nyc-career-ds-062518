from models import *
from sqlalchemy import create_engine

engine = create_engine('sqlite:///actors.db')

Session = sessionmaker(bind=engine)
session = Session()


def return_gwyneth_paltrows_roles():
    gwyn =  session.query(Actor).filter_by(name='Gwyneth Paltrow').all()[0]
    return gwyn.roles

def return_tom_hanks_2nd_role():
    hanx = session.query(Actor).filter_by(name='Tom Hanks').all()[0]
    return hanx.roles[1]
