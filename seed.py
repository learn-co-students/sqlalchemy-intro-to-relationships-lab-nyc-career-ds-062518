from models import *
from sqlalchemy import create_engine

engine = create_engine('sqlite:///actors.db')

Session = sessionmaker(bind=engine)
session = Session()

# add and commit the actors and roles below
tom_hanks=Actor(name= 'Tom Hanks')
tom_hanks.roles = [Role(character= 'Forrest Gump'), Role(character= 'Jim Lovell'),Role(character='Woody'), Role(character='Robert Langdon')]
session.add(tom_hanks)

gwyneth_paltrow= Actor(name='Gwyneth Paltrow')
gwyneth_paltrow.roles=[Role(character= 'Pepper Potts'), Role(character= 'Margot Tenenbaum')]
session.add(gwyneth_paltrow)

ryan_reynolds = Actor(name = 'Ryan Reynolds')
ryan_reynolds.roles=[Role(character='Deadpool'), Role(character='Wade Wilson')]
session.add(ryan_reynolds)


session.commit()
