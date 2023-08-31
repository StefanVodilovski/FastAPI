from typing import List, Optional
from sqlalchemy.orm import Session
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from .. import models,schemas,oAuth2
from ..database import  get_db

router = APIRouter(
    prefix="/votes",
    tags=["votes"]
)


@router.post("/")
def create_vote(vote: schemas.Vote, db: Session = Depends(get_db), current_user: int = Depends(oAuth2.get_current_user)):
    
    post = db.query(models.Post).filter(models.Post.id == vote.post_id).first()
    if post is None:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post wasnt found" )
    
    vote_query = db.query(models.Votes).filter(models.Votes.users_id == current_user.id, models.Votes.posts_id == vote.post_id) # type: ignore
        
    
    found_vote = vote_query.first()
    if vote.dir==1 :
        if found_vote:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"user {current_user.id} already liked the post" ) # type: ignore
        new_vote = models.Votes(users_id =current_user.id, posts_id = vote.post_id ) # type: ignore
        db.add(new_vote)
        db.commit()
        return {"message": "successfully added vote"}
    else:
        if not found_vote:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"vote wasnt found" )
    
        vote_query.delete(synchronize_session=False)
        db.commit()
        return {"message": "successfully deleted vote"}