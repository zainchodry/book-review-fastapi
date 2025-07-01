from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import schemas, crud, models, auth
from app.database import get_db

router = APIRouter(tags=["books"])

@router.post("/books", response_model=schemas.Book)
def add_book(
    book: schemas.BookCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_user)
):
    return crud.create_book(db, book)

@router.get("/books", response_model=list[schemas.Book])
def list_books(db: Session = Depends(get_db)):
    return crud.get_books(db)