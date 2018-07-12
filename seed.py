from models import *
from sqlalchemy import create_engine

engine = create_engine('sqlite:///actors.db')

Session = sessionmaker(bind=engine)
session = Session()

tom_hanks = Actor(name = "Tom Hanks")
gwyneth_paltrow = Actor(name = "Gwyneth Paltrow")
adam_sandler = Actor(name = "Adam Sandler")

tom_hanks.roles = [Role(character='Forrest Gump'), Role(character='Jim Lovell'),Role(character='Woody'), Role(character='Robert Langdon')]
gwyneth_paltrow.roles = [Role(character='Pepper Potts'), Role(character='Margot Tenenbaum')]
adam_sandler.roles = [Role(character="Happy Gilmore"), Role(character="Sonny Koufax")]

session.add_all([tom_hanks, gwyneth_paltrow, adam_sandler])
session.commit()
# session.add(tom_hanks.roles)
# session.add(gwyneth_paltrow.roles)
# session.add(adam_sandler.roles)
# session.commit()

# add and commit the actors and roles below
