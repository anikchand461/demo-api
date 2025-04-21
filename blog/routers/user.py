from fastapi import APIRouter, HTTPException, Response, Depends, status
from typing import List
from .. import schemas, models, database
from ..hashing import Hash
from sqlalchemy.orm import Session
from ..repository import user

router = APIRouter(
    prefix='/user',
    tags=['Users']
)

get_db = database.get_db

@router.post('/', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db : Session = Depends(get_db)):
    return user.create(request, db)

@router.get('/', response_model=List[schemas.User])
def get_all_users(db: Session = Depends(get_db)):
    return user.get_all_users(db)

@router.get('/{id}', response_model=schemas.ShowUser)
def get_user(id: int, db: Session = Depends(get_db)):
    return user.get_user(id, db)