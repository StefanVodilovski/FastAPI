
from sqlalchemy.orm import Session
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from .. import models,schemas, utils
from ..database import engine, get_db

router = APIRouter(
    prefix="/users",
    tags=['Users']
)

@router.post("/", response_model=schemas.UserResponse, status_code= status.HTTP_201_CREATED)
def add_user(new_user: schemas.UserBase, db: Session = Depends(get_db)):
    hashed_pass = utils.hash(new_user.password)
    new_user.password = hashed_pass
    
    create_new_user = models.User(**new_user.model_dump())
    db.add(create_new_user)
    db.commit()
    db.refresh(create_new_user)
    
    return create_new_user

@router.get("/{id}", response_model=schemas.UserResponse)
def get_user(id: int,  db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if user is None:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail= f'no user with id:{id}')
    
    return user


