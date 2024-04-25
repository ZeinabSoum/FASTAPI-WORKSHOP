from fastapi import FastAPI, APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import Base, get_db
from sqlalchemy import Column, Integer, String, ForeignKey
import schemas, models


route = APIRouter()


# Add new use
@route.post("/user")
def add_user(request: schemas.user, db: Session = Depends(get_db)):
    
    new_user= models.bookuser (id = request.id,
            
                            first_name  =  request. first_name ,
                           last_name = request. last_name,
                           gender = request. gender,
                           roles = request. roles
                        )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

# Retrieve a list of all users:
@route.get("/api/v1/users")
def all_users(request: schemas.user, db: Session = Depends(get_db)):
    return db

# Retrieve details for a specific user:

# Update an existing user:

# delete an existing user:
