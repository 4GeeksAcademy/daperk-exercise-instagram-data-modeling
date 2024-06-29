import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Text, DateTime, func
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True ,nullable=False)
    email = Column(String(100), nullable=False)
    password = Column(String(100), nullable=False)
    created_at = Column(DateTime, default=func.now())
    post = relationship('Post', back_populates='user')
    comments = relationship('Comment', back_populates='user')
    likes = relationship('Like', back_populates='user')



class Post(Base):
    __tablename__ = 'posts'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users_id'), nullable=False)
    img_url = Column(String(255), nullable=False)
    caption = Column('Text', nullable=True)
    created_at = Column(DateTime, default=func.now())
    user = relationship('User', back_populates='posts')
    comments = relationship('Comment', back_populates='post')
    likes = relationship('like', back_populates='post')

    
class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key= True)
    user_id = Column(Integer, ForeignKey('users_id'), nullable= False)
    post_id = Column(Integer, ForeignKey('posts.id'), nullable=False)
    text = Column(Text, nullable=False)
    creeated_at = Column(DateTime, default=func.now())
    user = relationship('User', back_populates='comments')
    post = relationship('Post', back_populates='comments')

class Like(Base):
    __tablename__ = 'likes'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    post_id = Column(Integer, ForeignKey('posts.id'), nullable=False)
    created_at = Column(DateTime, default=func.now())
    user = relationship('User', back_populates='likes')
    post = relationship('Post', back_populates='likes')


## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
