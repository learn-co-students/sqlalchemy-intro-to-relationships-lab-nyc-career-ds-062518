from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()


# write the Role and Actor classes below

class Actor(Base):
    __tablename__ = "actors"
    id = Column(INTEGER, primary_key=True)
    name = Column(TEXT)

    roles = relationship("Role", order_by = "Role.id", back_populates = "actor")

    # movies = relationship(Movie, secondary = Role, back_populates = "actors")

class Role(Base):
    __tablename__ = "roles"
    id = Column(INTEGER, primary_key=True)
    character = Column(TEXT)
    actor_id = Column(INTEGER, ForeignKey('actors.id'))
    actor = relationship(Actor, back_populates = "roles")

#     movie_id = Column(INTEGER, ForeignKey('movies.id'))
#
# class Movie(Base):
#     __tablename__ = "movies"
#     id = Column(INTEGER, primary_key=True)
#     name = Column(TEXT)
#
#     actors = relationship(Actor,secondary = Role, back_populates = "actors")

engine = create_engine('sqlite:///actors.db', echo = True)
Base.metadata.create_all(engine)
