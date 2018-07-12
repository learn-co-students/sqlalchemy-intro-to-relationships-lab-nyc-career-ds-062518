from models import *
from sqlalchemy import create_engine

engine = create_engine('sqlite:///actors.db')

Session = sessionmaker(bind=engine)
session = Session()


def return_gwyneth_paltrows_roles():
    gp = session.query(Actor).filter_by(name ='Gwyneth Paltrow').first()
    return gp.roles


def return_tom_hanks_2nd_role():
    th = session.query(Actor).filter_by(name = 'Tom Hanks').first()
    return th.roles[1]
