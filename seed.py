from models import *
from sqlalchemy import create_engine

engine = create_engine('sqlite:///actors.db')

Session = sessionmaker(bind=engine)
session = Session()

Ewan_McGreggor = Actor(name = 'Ewan McGreggor')
Obi_Wan = Role(character = 'Obi Wan')
Christopher_Robin = Role(character = 'Christopher Robin')

Tom_Hanks = Actor(name = 'Tom Hanks')
Forrest_Gump = Role(character = 'Forrest Gump')
Jim_Lovell = Role(character = 'Jim Lovell')
Woody = Role(character = 'Woody')
Robert_Langdon = Role(character = 'Robert Langdon')

Gwyneth_Paltrow = Actor(name = 'Gwyneth Paltrow')

Gwyneth_Paltrow.roles = [Role(character = 'Pepper Potts'), Role(character = 'Margot Tenenbaum')]
Tom_Hanks.roles = [Forrest_Gump, Jim_Lovell, Woody, Robert_Langdon]
Ewan_McGreggor.roles = [Obi_Wan, Christopher_Robin]
# add and commit the actors and roles below

session.add_all([Ewan_McGreggor,
                Tom_Hanks,
                Gwyneth_Paltrow])
session.commit()
