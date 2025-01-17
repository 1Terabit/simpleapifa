from pydantic import BaseModel

class CommentBase(BaseModel):
    item_id: int
    user_id: int
    content: str

class CommentCreate(CommentBase):
    pass

class CommentResponse(CommentBase):
    id: int

    class Config:
        from_attributes = True  #NOTE Cambiar 'orm_mode' a 'from_attributes' si usas Pydantic V2 