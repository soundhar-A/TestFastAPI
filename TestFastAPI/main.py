from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
import models
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

class AddressBase(BaseModel):
    latitude: float
    longitude: float
    description: str

class AddressCreate(AddressBase):
    pass

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/addresses/", response_model=AddressBase)
def create_address(address: AddressCreate, db: Session = Depends(get_db)):
    db_address = models.Address(**address.dict())
    db.add(db_address)
    db.commit()
    db.refresh(db_address)
    return db_address

@app.get("/addresses/")
def read_addresses(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    addresses = db.query(models.Address).offset(skip).limit(limit).all()
    return addresses

# Additional endpoints for update, delete, and distance-based retrieval can be added similarly
