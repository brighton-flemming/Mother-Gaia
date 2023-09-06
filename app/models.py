from sqlalchemy import Column, Integer, String, ForeignKey, Text, UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False, unique=True)
    age = Column(Integer, nullable=False,unique=True)
    email = Column(String, nullable=True)

    bottles = relationship('Bottle', back_populates='user')
    trees = relationship('Tree', back_populates='user')
    recommendations = relationship('Recommendation', back_populates='user')

class Bottle(Base):
    __tablename__ = 'bottles'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    user_id =  Column(Integer, ForeignKey('users.id'), nullable=False)
    bottles_recycled = Column(Integer, nullable=False, default=0)

    user = relationship('User', back_populates='bottles')

    UniqueConstraint('users.id', 'bottles_recycled', name='unique_user_bottles')

class Tree(Base):
    __tablename__ = 'bottles'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    trees_planted = Column(Integer, nullable=False, default=0)

    user = relationship('User', back_populates='trees')

class Recommendation(Base):
    __tablename__ = 'recommendations'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    recommendation_text = Column(Text, nullable=False)

    user = relationship('User', back_populates='trees')





