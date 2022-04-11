import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

#     def to_dict(self):
#         return {}

class User (Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    name = Column(String(50))
    phone_number = Column(String(50))
    email = Column(String(50), nullable=False)
    favorite = relationship('Favorite', backref='user')

class Card (Base):
    __tablename__ = 'card'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    image = Column(String(50))
    description = Column(String(50))
    character = relationship('Character', backref='card')

class Character (Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(Integer, ForeignKey('card.name'))
    image = Column(Integer, ForeignKey('card.image'))
    description = Column(Integer, ForeignKey('card.description'))
    birth_date = Column(String(50))
    gender = Column(String(50))
    height = Column(String(50))
    skin_color = Column(String(50))
    eye_color = Column(String(50))

class Vehicle (Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True)
    name = Column(Integer, ForeignKey('card.name'))
    image = Column(Integer, ForeignKey('card.image'))
    description = Column(Integer, ForeignKey('card.description'))
    model = Column(String(50))
    passengers = Column(String(50))
    lenght = Column(String(50))
    cargo_capacity = Column(String(50))
    consumables = Column(String(50))

class Planet (Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(Integer, ForeignKey('card.name'))
    image = Column(Integer, ForeignKey('card.image'))
    description = Column(Integer, ForeignKey('card.description'))
    climate = Column(String(50))
    population = Column(String(50))
    orbital_period = Column(String(50))
    rotation_period = Column(String(50))
    diameter = Column(String(50))

class Favorite (Base):
    __tablename__= 'favorite'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    card_id = Column(Integer, ForeignKey('card.id'))


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')