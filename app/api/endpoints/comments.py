from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..dependencies import get_db
from ...schemas.comment import CommentCreate, CommentResponse
from ...services.comment_service import create_comment, get_comment_by_id, delete_comment, update_comment

router = APIRouter()

@router.post("/", response_model=CommentResponse)
def create_comment_endpoint(comment: CommentCreate, db: Session = Depends(get_db)):
    return create_comment(db=db, comment=comment) 

@router.get("/{comment_id}", response_model=CommentResponse)
def read_comment(comment_id: int, db: Session = Depends(get_db)):
    comment = get_comment_by_id(db=db, comment_id=comment_id)
    if comment is None:
        raise HTTPException(status_code=404, detail="Comment not found")
    return comment 

@router.delete("/{comment_id}", response_model=CommentResponse)
def delete_comment_endpoint(comment_id: int, db: Session = Depends(get_db)):
    comment = delete_comment(db=db, comment_id=comment_id)
    if comment is None:
        raise HTTPException(status_code=404, detail="Comment not found")
    return comment 

@router.put("/{comment_id}", response_model=CommentResponse)
def update_comment_endpoint(comment_id: int, comment: CommentCreate, db: Session = Depends(get_db)):
    updated_comment = update_comment(db=db, comment_id=comment_id, comment=comment)
    if updated_comment is None:
        raise HTTPException(status_code=404, detail="Comment not found")
    return updated_comment 