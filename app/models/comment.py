from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship
from ..database import Base

class Comment(Base):
    __tablename__ = "comments"
    __table_args__ = {'schema': 'items'}
    
    id = Column(Integer, primary_key=True, index=True)
    item_id = Column(Integer, ForeignKey("items.items.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("items.users.id"), nullable=False)
    content = Column(Text, nullable=False)

    item = relationship("Item", back_populates="comments")
    user = relationship("User") 