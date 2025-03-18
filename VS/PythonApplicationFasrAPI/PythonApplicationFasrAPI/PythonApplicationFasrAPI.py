'''
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker
from sqlalchemy import  Column, Integer, String
 
from fastapi import FastAPI
 
SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
 
 
class Base(DeclarativeBase): pass
class Person(Base):
    __tablename__ = "people"
 
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer,)
 
SessionLocal = sessionmaker(autoflush=False, bind=engine)
'''

from database import *
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, Body
from fastapi.responses import JSONResponse, FileResponse
 
Base.metadata.create_all(bind=engine)
 
app = FastAPI()
 
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
  

@app.get("/")
def main():
    return FileResponse("public/index.html")
  

@app.get("/api/users")
def get_people(db: Session = Depends(get_db)):
    return db.query(Person).all()
  

@app.get("/api/users/{id}")
def get_person(id, db: Session = Depends(get_db)):
    person = db.query(Person).filter(Person.id == id).first()
    if person==None:  
        return JSONResponse(status_code=404, content={ "message": "Пользователь не найден"})
    return person
  
  
@app.post("/api/users")
def create_person(data  = Body(), db: Session = Depends(get_db)):
    person = Person(name=data["name"], age=data["age"])
    db.add(person)
    db.commit()
    db.refresh(person)
    return person
  

@app.put("/api/users")
def edit_person(data  = Body(), db: Session = Depends(get_db)):
   
    person = db.query(Person).filter(Person.id == data["id"]).first()
    if person == None: 
        return JSONResponse(status_code=404, content={ "message": "Пользователь не найден"})
    person.age = data["age"]
    person.name = data["name"]
    db.commit()
    db.refresh(person)
    return person
  
  
@app.delete("/api/users/{id}")
def delete_person(id, db: Session = Depends(get_db)):
    person = db.query(Person).filter(Person.id == id).first()
   
    if person == None:
        return JSONResponse( status_code=404, content={ "message": "Пользователь не найден"})
   
    db.delete(person)
    db.commit()
    return person


@app.delete("/api/users/{id}")
def delete_person(id, db: Session = Depends(get_db)):
    person = db.query(Person).filter(Person.id == id).first()
   
    if person == None:
        return JSONResponse( status_code=404, content={ "message": "Пользователь не найден"})
   
    db.delete(person)
    db.commit()
    return person


@app.put("/api/users")
def edit_person(data  = Body(), db: Session = Depends(get_db)):
   
    person = db.query(Person).filter(Person.id == data["id"]).first()
    if person == None: 
        return JSONResponse(status_code=404, content={ "message": "Пользователь не найден"})
    person.age = data["age"]
    person.name = data["name"]
    db.commit()
    db.refresh(person)
    return person


def happened():
    if 1 > 2:
        print("Some Wrong (LuL)")
    else:
        print("Nothing happened")


