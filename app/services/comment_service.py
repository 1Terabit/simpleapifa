from sqlalchemy.orm import Session
from ..models.comment import Comment
from ..schemas.comment import CommentCreate

def create_comment(db: Session, comment: CommentCreate):
    db_comment = Comment(**comment.dict())
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment

def get_comment_by_id(db: Session, comment_id: int):
    return db.query(Comment).filter(Comment.id == comment_id).first()  #NOTE Busca el comentario por ID 

def delete_comment(db: Session, comment_id: int):
    comment = db.query(Comment).filter(Comment.id == comment_id).first()
    if comment:
        db.delete(comment)
        db.commit()
        return comment
    return None 

def update_comment(db: Session, comment_id: int, comment: CommentCreate):
    db_comment = db.query(Comment).filter(Comment.id == comment_id).first()
    if db_comment:
        db_comment.item_id = comment.item_id
        db_comment.user_id = comment.user_id
        db_comment.content = comment.content
        db.commit()
        db.refresh(db_comment)
        return db_comment
    return None 