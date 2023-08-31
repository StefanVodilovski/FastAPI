from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, conint
      
class UserBase(BaseModel):
    email: EmailStr
    password: str
    
class UserResponse(BaseModel):
    id: int
    email: EmailStr 
    created_at: datetime

class UserLogin(BaseModel):
    email: EmailStr
    password: str
    
    
class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True
    
class PostCreate(PostBase):
    pass
    
class PostResponse(PostBase):
    id:int
    created_at: datetime
    
    owner_id: int
    owner: UserResponse 
    
class PostJoin(BaseModel):
    Post: PostResponse
    votes: int       
    
    
class Token(BaseModel):
    access_token: str
    # token_type: str  
    
class TokenData(BaseModel):
    id: Optional[str] = None    
       
    
class Vote(BaseModel):
    post_id : int
    dir: conint(le=1)