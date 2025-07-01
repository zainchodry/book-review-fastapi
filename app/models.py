from app.database import Base
from sqlalchemy import Integer, String, Column, ForeignKey, Float
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), unique=True, index=True)
    password = Column(String)
    reviews = relationship("Review", back_populates="user")

class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, index=True, primary_key=True)
    title = Column(String(100), index=True)
    author = Column(String)
    reviews = relationship("Review", back_populates="book")

class Review(Base):
    __tablename__ = "reviews"
    id = Column(Integer, primary_key=True, index=True)
    rating = Column(Float)
    comment = Column(String)
    book_id = Column(Integer, ForeignKey("books.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    book = relationship("Book", back_populates="reviews")
    user = relationship("User", back_populates="reviews")