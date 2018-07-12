from models import *
from sqlalchemy import create_engine

engine = create_engine('sqlite:///actors.db')

Session = sessionmaker(bind=engine)
session = Session()



tom_hanks = Actor(name = "Tom Hanks")
tom_hanks.roles = [Role(character = 'Forrest Gump'), Role(character = "Jim Lovell"), Role(character = "Woody"), Role(character = "Robert Langdon")]

gwyneth_paltrow = Actor(name = "Gwyneth Paltrow")
gwyneth_paltrow.roles = [Role(character = "Pepper Potts"), Role(character = "Margot Tenenbaum")]

ewan_mcgregor = Actor(name = "Ewan McGregor")
ewan_mcgregor.roles = [Role(character = "Obi Wan Kenobi"), Role(character = "Christopher Robin")]

# pooh = Movie(name = "Pooh")

session.add_all([tom_hanks, gwyneth_paltrow, ewan_mcgregor])
session.commit()


# add and commit the actors and roles below
