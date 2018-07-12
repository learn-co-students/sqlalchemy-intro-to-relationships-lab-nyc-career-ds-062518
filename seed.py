from models import *
from sqlalchemy import create_engine

engine = create_engine('sqlite:///actors.db')

Session = sessionmaker(bind=engine)
session = Session()

tom_hanks = Actor(name='Tom Hanks')
tom_hanks.roles = [Role(character='Forrest Gump'), Role(character='Jim Lovell'),
Role(character='Woody'), Role(character='Robert Langdon')]

gwyneth_paltrow = Actor(name='Gwyneth Paltrow')
gwyneth_paltrow.roles = [Role(character='Pepper Potts'), Role(character='Margot Tenenbaum')]

brad_pitt = Actor(name='Brad Pitt')
brad_pitt.roles = [Role(character='John Smith'), Role(character='Rusty Ryan')]

session.add(tom_hanks)
session.add(gwyneth_paltrow)
session.add(brad_pitt)
session.commit()
