from models import *
from sqlalchemy import create_engine

engine = create_engine('sqlite:///actors.db')

Session = sessionmaker(bind=engine)
session = Session()


def return_gwyneth_paltrows_roles():
    gwyneth = session.query(Actor).filter(Actor.name == 'Gwyneth Paltrow').first()
    return gwyneth.roles

def return_tom_hanks_2nd_role():
    tom = session.query(Actor).filter(Actor.name == 'Tom Hanks').first()
    return tom.roles[1]
