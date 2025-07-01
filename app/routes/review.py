from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import schemas, crud, models, auth
from app.database import get_db

router = APIRouter(tags=["reviews"])

@router.post("/reviews", response_model=schemas.Review)
def post_review(
    review: schemas.ReviewCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_user)
):
    return crud.create_review(db, review, current_user.id)

@router.get("/books/{book_id}/reviews")
def get_book_reviews(book_id: int, db: Session = Depends(get_db)):
    reviews = crud.get_reviews_for_book(db, book_id)
    avg = crud.get_average_rating(db, book_id)
    return {"average_rating": avg, "reviews": reviews}