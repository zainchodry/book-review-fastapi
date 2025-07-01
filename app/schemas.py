from pydantic import BaseModel
from typing import List, Optional

class UserCreate(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    id: int
    username: str
    class Config:
        orm_mode = True  

class BookBase(BaseModel):
    title: str
    author: str

class BookCreate(BookBase):
    pass

class Book(BookBase):
    id: int
    class Config:
        orm_mode = True

class ReviewBase(BaseModel):
    rating: float
    comment: str

class ReviewCreate(ReviewBase):
    book_id: int

class Review(ReviewBase):
    id: int
    user_id: int
    class Config:
        orm_mode = True