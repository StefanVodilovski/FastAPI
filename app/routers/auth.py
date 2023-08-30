from sqlalchemy.orm import Session
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from .. import models,schemas, utils, oAuth2
from ..database import engine, get_db

router = APIRouter(
    tags=['Authentication']
)

router = APIRouter()

@router.post("/login", response_model=schemas.Token)
def login_attempt(user_creds: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db) ):
    login_user = db.query(models.User).filter(models.User.email == user_creds.username).first()
    
    if login_user is None:
        raise HTTPException(status_code= status.HTTP_403_FORBIDDEN, detail= "Invalid Credentials")
    
    
    if not utils.verify(user_creds.password, login_user.password):
        raise HTTPException(status_code= status.HTTP_403_FORBIDDEN, detail= "Invalid Credentials")
    
    #create token
    access_token = oAuth2.create_access_token(data = {"user_id": login_user.id})
    #login token
    
    return {"access_token":access_token}