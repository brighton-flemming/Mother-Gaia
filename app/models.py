from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from . import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False, unique=True)
    age = Column(Integer, nullable=False,unique=True)
    email = Column(String, nullable=True)
    bottles = relationship('Bottle', back_populates='user')

class Bottle(Base):
    __tablename__ = 'bottles'

    id = Column(Integer, primary_key=True)
    user_id =  Column(Integer, ForeignKey('users.id'), nullable=False)
    bottles_recycled = Column(Integer, nullable=False, default=0)

    user = relationship('User', back_populates='bottles')

class Tree(Base):
    __tablename__ = 'bottles'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    trees_planted = Column(Integer, nullable=False, default=0)

    user = relationship('User', back_populates='trees')

class Recommendations(Base):
    __tablename__ = 'recommendations'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    recommendation_text = Column(String(200), nullable=False)

    user = relationship('User', back_populates='trees')





