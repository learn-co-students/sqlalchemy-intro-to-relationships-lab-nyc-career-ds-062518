from models import *
from sqlalchemy import create_engine

engine = create_engine('sqlite:///actors.db')

Session = sessionmaker(bind=engine)
session = Session()


def return_gwyneth_paltrows_roles():
    parts = session.query(Actor).filter_by(name= "Gwyneth Paltrow").first()
    return parts.roles

def return_tom_hanks_2nd_role():
    parts = session.query(Actor).filter_by(name= "Tom Hanks").first()
    return parts.roles[1]
