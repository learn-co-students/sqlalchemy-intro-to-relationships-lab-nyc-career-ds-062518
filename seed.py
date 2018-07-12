from models import *
from sqlalchemy import create_engine

engine = create_engine('sqlite:///actors.db')

Session = sessionmaker(bind=engine)
session = Session()

tom_hanks = Actor(name='Tom Hanks')
gwyneth_paltrow = Actor(name='Gwyneth Paltrow')
nic_cage = Actor(name='Nic Cage')

actors = [tom_hanks,gwyneth_paltrow,nic_cage]

forrest_gump = Role(character='Forrest Gump', actor_id=1)
jim_lovell = Role(character='Jim Lovell', actor_id=1)
woody = Role(character='Woody', actor_id=1)
robert_langdon = Role(character='Robert Langdon', actor_id=1)

pepper_potts = Role(character='Pepper Potts', actor_id=2)
margot_tenenbaum= Role(character='Margot Tenenbaum', actor_id=2)

castor_troy= Role(character='Castor Troy', actor_id=3)
stanley_goodspeed= Role(character='Stanley Goodspeed', actor_id=3)

roles = [forrest_gump,jim_lovell,woody,robert_langdon,pepper_potts,margot_tenenbaum,castor_troy,stanley_goodspeed]

if len(session.query(Actor).all()) == 0:
    session.add_all(actors)
    session.commit()

if len(session.query(Role).all()) == 0:
    session.add_all(roles)
    session.commit()
