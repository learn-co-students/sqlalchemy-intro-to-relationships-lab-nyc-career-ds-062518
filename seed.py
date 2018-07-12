from models import *
from sqlalchemy import create_engine

engine = create_engine('sqlite:///actors.db')

Session = sessionmaker(bind=engine)
session = Session()

# add and commit the actors and roles below

tom_hanks = Actor(name = "Tom Hanks")
tom_hanks.roles = [Role(character = "Forrest Gump"), Role(character = "Jim Lovell"), Role(character = "Woody"), Role(character = "Robert Langdon")]

gwyneth_paltrow = Actor(name = "Gwyneth Paltrow")
gwyneth_paltrow.roles = [Role(character = "Pepper Potts"), Role(character = "Margot Tenenbaum")]

sam_jackson = Actor(name = "Samuel Jackson")
sam_jackson.roles = [Role(character = "Jules Winnfield"), Role(character = "Mace Windu")]

session.add(tom_hanks)
session.add(gwyneth_paltrow)
session.add(sam_jackson)
session.commit()
