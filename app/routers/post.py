
from typing import List, Optional
from sqlalchemy import func
from sqlalchemy.orm import Session
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from .. import models,schemas,oAuth2
from ..database import  get_db


router = APIRouter(
    prefix="/posts",
    tags=['Posts']
)

@router.get("/", response_model = List[schemas.PostJoin])
async def get_all_posts(db: Session = Depends(get_db), user_id: int = Depends(oAuth2.get_current_user), limit: int = 10,
                        search: Optional[str] = "",skip : int = 0 ):
    # cursor.execute("""SELECT * FROM posts""")
    # posts = cursor.fetchall()
    #  db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
    
    posts = db.query(models.Post, func.count(models.Votes.posts_id).label("votes")).join(models.Votes, models.Votes.posts_id == models.Post.id, isouter= True).group_by(models.Post.id).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
    
    if not posts:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail= "db is empty ")
    
    # response_data = [
    #     {"post": post, "votes": votes} for post, votes in posts
    # ]

    return posts

@router.get("/{id}", response_model=schemas.PostJoin)
async def get_post(id: int, db: Session = Depends(get_db), user_id: int = Depends(oAuth2.get_current_user)):
    # cursor.execute("""SELECT * FROM posts where id = %s""", (str(id),))
    # post = cursor.fetchone()
    post = db.query(models.Post, func.count(models.Votes.users_id).
                     label('votes')).join(models.Votes, models.Votes.posts_id == models.Post.id,isouter= True).group_by(models.Post.id).filter(models.Post.id == id).first()
    
    if post is None:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail= "no post with that id")
    
    return post


@router.post("/", status_code= status.HTTP_201_CREATED, response_model=schemas.PostResponse)
async def new_post(post: schemas.PostCreate, db: Session = Depends(get_db), user_id: int = Depends(oAuth2.get_current_user)):
    # cursor.execute("""INSERT INTO posts(title, content, published) VALUES(%s, %s, %s)""",( post.title, post.content, post.published))
    # post = cursor.fetchone() # type: ignore
    # conn.commit()
    print(user_id)
    created_new_post = models.Post(owner_id = user_id.id ,**post.model_dump())
    db.add(created_new_post)
    db.commit()
    db.refresh(created_new_post)

    return created_new_post

@router.delete("/{id}", status_code= status.HTTP_204_NO_CONTENT)
def delete_post(id:int, db: Session = Depends(get_db), user_id: int = Depends(oAuth2.get_current_user)):
    # cursor.execute("""DELETE FROM posts WHERE id = %s""", (str(id),))
    # del_post = cursor.fetchone()
    # conn.commit()
    del_post = db.query(models.Post).filter(models.Post.id == id)    
    
    post = del_post.first()
    
    if post == None:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail= "no post with that id") 
    
    if post.owner_id != user_id.id:
        raise HTTPException(status_code= status.HTTP_403_FORBIDDEN, detail= "can't delete this post, not authorized") 
    
    post.delete(synchronize_session=False)
    
    db.commit()
    
    return Response(status_code= status.HTTP_204_NO_CONTENT)


@router.put("/{id}", response_model=schemas.PostResponse)
def update_post(id: int, updated_post:schemas.PostCreate,  db: Session = Depends(get_db), user_id: int = Depends(oAuth2.get_current_user)):
    # cursor.execute("""UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s""", (post.title,post.content,post.published,str(id)))
    # updated_post = cursor.fetchone()
    # conn.commit()
    post_query = db.query(models.Post).filter(models.Post.id == id )
    post = post_query.first()
    
    if post == None:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail= "no post with that id") 
    
    if post.owner_id != user_id.id: # type: ignore
        raise HTTPException(status_code= status.HTTP_403_FORBIDDEN, detail= "can't change this post, not authorized")
    
    post_query.update(updated_post.model_dump(), synchronize_session=False) # type: ignore
    db.commit()
    
    return post_query.first()