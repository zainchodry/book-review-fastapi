from fastapi import FastAPI
from app.database import Base,engine
from app.routes import book, user, review

Base.metadata.create_all(bind=engine)


app = FastAPI(title = "Book Review System")

app.include_router(user.router)
app.include_router(book.router)
app.include_router(review.router)

