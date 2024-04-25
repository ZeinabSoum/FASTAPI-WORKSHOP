from fastapi import FastAPI, APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import Base, get_db
from sqlalchemy import Column, Integer, String, ForeignKey
import schemas, models


route = APIRouter()

# Add new book
@route.post("/books")
def add_book(request: schemas.book, db: Session = Depends(get_db)):
    
    new_book = models.book (title = request.title,
                           author =  request.author,
                           description = request.description,
                           published_year = request.published_year,
                           publisher = request.publisher
                        )

    db.add(new_book)
    db.commit()
    db.refresh(new_book)

    return new_book

# Retrieve a list of all books:
@route.post("/books")
def get_book(request: schemas.book, db: Session = Depends(get_db)):
    
    get_book = models.book (title = request.title,
                           author =  request.author,
                           description = request.description,
                           published_year = request.published_year,
                           publisher = request.publisher
                        )

    db.add(get_book)
    db.commit()
    db.refresh(get_book)

    return get_book

# Retrieve details for a specific book:
@route.get("/api/v1/book")
def all_book(request: schemas.book, db: Session = Depends(get_db)):
    return db

# Update an existing book:

# delete an existing book: