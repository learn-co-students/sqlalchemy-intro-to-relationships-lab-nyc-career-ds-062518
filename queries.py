from models import *
from sqlalchemy import create_engine

engine = create_engine('sqlite:///actors.db')

Session = sessionmaker(bind=engine)
session = Session()


def return_gwyneth_paltrows_roles():
    gwen = session.query(Actor).filter_by(name ='Gwyneth Paltrow').first()
    return gwen.roles

def return_tom_hanks_2nd_role():
    tom=session.query(Actor).filter_by(name ='Tom Hanks').first()
    return tom.roles[1]
