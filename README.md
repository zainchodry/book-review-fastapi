# 📚 Book Review System – FastAPI Project

This is a simple **Book Review API** built with **FastAPI**, **SQLAlchemy**, **JWT authentication**, and **SQLite**.  
Users can register, log in, add books, and submit reviews.

---

## 🚀 Features

✅ User registration and login  
✅ Secure authentication using JWT  
✅ Add and list books  
✅ Post reviews for any book  
✅ Get average ratings for each book  
✅ Modular and scalable architecture

---

## 🧱 Technologies Used

- FastAPI
- SQLAlchemy
- Pydantic
- SQLite
- JWT (with `python-jose`)
- `passlib` for password hashing

---

## 📂 Project Structure

book-review-fastapi/
│
├── app/
│ ├── init.py
│ ├── auth.py # JWT and auth logic
│ ├── crud.py # Business logic (create/read)
│ ├── database.py # DB setup
│ ├── models.py # SQLAlchemy models
│ ├── schemas.py # Pydantic models
│ └── routes/
│ ├── book.py # /books endpoints
│ ├── user.py # /register and /login
│ └── review.py # /reviews endpoints
│
├── main.py # FastAPI app entry point
├── requirements.txt # Dependencies
├── .gitignore
└── README.md


---

## 🔑 Authentication

All `/books` and `/reviews` endpoints are protected and require a valid **Bearer Token**.

### 🔐 Token Flow:
1. `POST /register` → to register a user
2. `POST /token` → to log in and get a token
3. Use token as:



---

## 🛠️ Setup Instructions

1. **Clone the repo:**
   ```bash
   git clone https://github.com/yourusername/book-review-fastapi.git
   cd book-review-fastapi

2. #Create a virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

3. #Install dependencies
pip install -r requirements.txt


4. #Run the app
uvicorn main:app --reload
