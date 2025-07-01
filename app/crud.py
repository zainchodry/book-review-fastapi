from sqlalchemy.orm import Session
from app import models, schemas,auth
from sqlalchemy import func

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = auth.hash_password(user.password)
    db_user = models.User(username=user.username, password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_book(db: Session, book: schemas.BookCreate):
    db_book = models.Book(**book.model_dump())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def get_books(db: Session):
    return db.query(models.Book).all()

def create_review(db: Session, review: schemas.ReviewCreate, user_id: int):
    db_review = models.Review(**review.model_dump(), user_id=user_id)
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review

def get_reviews_for_book(db: Session, book_id: int):
    return db.query(models.Review).filter(models.Review.book_id == book_id).all()

def get_average_rating(db: Session, book_id: int):
    return db.query(func.avg(models.Review.rating)).filter(models.Review.book_id == book_id).scalar()