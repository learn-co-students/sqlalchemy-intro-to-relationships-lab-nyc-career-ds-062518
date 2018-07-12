from models import *
from sqlalchemy import create_engine

engine = create_engine('sqlite:///actors.db')

Session = sessionmaker(bind=engine)
session = Session()

tom_hanks = Actor(name = "Tom Hanks")
gwyneth_paltrow = Actor(name = "Gwyneth Paltrow")
eric_idle = Actor(name = "Eric Idle")

forrest_gump = Role(character = 'Forrest Gump', actor_id =1)
jim_lovell = Role(character = 'Jim Lovell', actor_id = 1)
woody = Role(character = 'Woody', actor_id = 1)
robert_langdon = Role(character = 'Robert Langdon', actor_id = 1)
pepper_potts = Role(character = 'Pepper Potts',actor_id = 2)
margot_tenenbaum = Role(character = 'Margot Tenenbaum', actor_id = 2)
dead_collecter = Role(character = 'Dead Collecter',actor_id = 3)
rat = Role(character = 'Rat' ,actor_id = 3)

session.add(forrest_gump)
session.add(jim_lovell)
session.add(woody)
session.add(robert_langdon)
session.add(pepper_potts)
session.add(margot_tenenbaum)
session.add(dead_collecter)
session.add(rat)

session.add(tom_hanks)
session.add(gwyneth_paltrow)
session.add(eric_idle)

session.commit()
