from models import *
from sqlalchemy import create_engine

engine = create_engine('sqlite:///actors.db')

Session = sessionmaker(bind=engine)
session = Session()

# add and commit the actors and roles below
tom_hanks = Actor(name='Tom Hanks')
tom_hanks.roles= [Role(character = 'Forrest Gump'),Role(character= 'Jim Lovell'), Role(character='Woody'), Role(character= 'Robert Langdon')]
gwyneth_paltrow= Actor(name = 'Gwyneth Paltrow')
gwyneth_paltrow.roles = [Role(character='Pepper Potts'), Role(character= 'Margot Tenenbaum')]
blake_lively = Actor(name='Blake Lively')
blake_lively.roles = [Role(character= 'Serena'), Role(character = 'Bridget')]

session.add(tom_hanks)
session.add(gwyneth_paltrow)
session.add(blake_lively)
session.commit()
