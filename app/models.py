from sqlalchemy import Column, Integer, String, ForeignKey, Text, UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    age = Column(Integer, nullable=False)
    email = Column(String, nullable=False)

    bottles = relationship('Bottle', back_populates='users')
    trees = relationship('Tree', back_populates='users')
    recommendations = relationship('Recommendation', back_populates='users')

class Bottle(Base):
    __tablename__ = 'bottles'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    user_id =  Column(Integer, ForeignKey('users.id'), nullable=False)
    action = Column(String)
    bottles_recycled = Column(Integer, nullable=False, default=0)
    bottles_disposed = Column(Integer, nullable=False, default=0)
    trash_effect = Column(Integer)

    users = relationship('User', back_populates='bottles')

    UniqueConstraint('users.id', 'bottles_recycled', name='unique_user_bottles')

class Tree(Base):
    __tablename__ = 'trees'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    action = Column(String,  nullable=True)
    trees_planted = Column(Integer, nullable=False, default=0)
    trees_cut_down = Column(Integer, nullable=False, default=0)
    net_effect = Column(Integer, default=0)

    users = relationship('User', back_populates='trees')

class Recommendation(Base):
    __tablename__ = 'recommendations'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    recommendation_text = Column(Text, nullable=False)

    users = relationship('User', back_populates='recommendations')





