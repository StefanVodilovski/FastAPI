from sqlalchemy import Integer, Column, String, Boolean, DateTime, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from .database import Base

class Post(Base):
    __tablename__ = "posts"
    
    id = Column(Integer, primary_key=True, nullable = False)
    title = Column(String(50), nullable = False)
    content = Column(String(100), nullable = False)
    published = Column(Boolean, server_default='1', nullable = False)
    created_at = Column(TIMESTAMP(timezone=True), server_default= text('CURRENT_TIMESTAMP'))
    owner_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable= False)
    
    owner = relationship('User')
    
class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, nullable = False)
    email = Column(String(50), nullable = False, unique=True)
    password = Column(String(100), nullable = False)
    created_at = Column(TIMESTAMP(timezone=True), server_default= text('CURRENT_TIMESTAMP'))
        
        
class Votes(Base):
    __tablename__ = 'votes'
    
    users_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable= False, primary_key=True)
    posts_id = Column(Integer, ForeignKey("posts.id", ondelete="CASCADE"), nullable= False, primary_key=True)    
    
     