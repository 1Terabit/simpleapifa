from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from ..database import Base

class Item(Base):
    __tablename__ = "items"
    __table_args__ = {'schema': 'items'}
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(Text)

    comments = relationship("Comment", back_populates="item")  #NOTE: Relación inversa 