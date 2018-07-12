from models import *
from sqlalchemy import create_engine

engine = create_engine('sqlite:///actors.db')

Session = sessionmaker(bind=engine)
session = Session()


def return_gwyneth_paltrows_roles():
    gwyneth_id = session.query(Actor.id).filter_by(name = 'Gwyneth Paltrow').first()[0]
    return session.query(Role).filter_by(actor_id = gwyneth_id).all()

def return_tom_hanks_2nd_role():
    hanks_id = session.query(Actor.id).filter_by(name = 'Tom Hanks').first()[0]
    return session.query(Role).filter_by(actor_id = hanks_id).all()[1]
