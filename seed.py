from models import *
from sqlalchemy import create_engine

engine = create_engine('sqlite:///actors.db')

Session = sessionmaker(bind=engine)
session = Session()

# add and commit the actors and roles below
tom= Actor(name ="Tom Hanks")
gwyn = Actor(name= "Gwyneth Paltrow")
jim = Actor(name= "Jim Carrey")

tom.roles = [Role(character="Forrest Gump"),Role(character="Jim Lovell"),Role(character= "Woody"),Role(character= "Robert Langdon")]
gwyn.roles = [Role(character= "Pepper Potts"), Role(character= "Margot Tenenbaum")]
jim.roles = [Role(character ="Ace Ventura"),Role(character= "Lloyd Christmas")]
# forrest = Role(charachter="Forrest Gump", actor = tom)
# jiml = Role(charachter="Jim Lovell", actor = tom)
# woody = Role(charachter= "Woody", actor = tom)
# rob = Role(charachter= "Robert Langdon", actor = tom)
# pepper = Role(charachter= "Pepper Potts", actor = gwyn)
# margot = Role(charachter= "Margot Tenenbaum", actor = gwyn)
# ace = Role(charachter ="Ace Ventura", actor= jim)
# lloyd = Role( charachter= "Lloyd Christmas", actor = jim)

session.add(tom)
session.add(gwyn)
session.add(jim)
# session.(tom.roles)
# session.(gwyn.roles)
# session.(jim.roles)
session.commit()
