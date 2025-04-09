from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas
from .database import engine, get_db
from .middleware import ErrorHandlerMiddleware
from typing import List

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.add_middleware(ErrorHandlerMiddleware)


# Character endpoints
@app.post("/characters/", response_model=schemas.Character)
def create_character(character: schemas.CharacterCreate, db: Session = Depends(get_db)):
    db_character = models.Character(**character.dict())
    db.add(db_character)
    db.commit()
    db.refresh(db_character)
    return db_character

@app.get("/characters/", response_model=List[schemas.Character])
def read_characters(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    characters = db.query(models.Character).offset(skip).limit(limit).all()
    return characters

@app.post("/characters/{character_id}/relationships/", response_model=schemas.Character)
def create_relationship(
    character_id: str, 
    relationship: schemas.CharacterRelationshipCreate, 
    db: Session = Depends(get_db)
):
    db_character = db.query(models.Character).filter(models.Character.id == character_id).first()
    if not db_character:
        raise HTTPException(status_code=404, detail="Character not found")
    
    related_character = db.query(models.Character).filter(
        models.Character.id == relationship.related_character_id
    ).first()
    if not related_character:
        raise HTTPException(status_code=404, detail="Related character not found")
    
    # Add relationship
    db_character.relationships.append(related_character)
    db.commit()
    db.refresh(db_character)
    return db_character

# Character Group endpoints
@app.post("/groups/", response_model=schemas.CharacterGroup)
def create_group(group: schemas.CharacterGroupCreate, db: Session = Depends(get_db)):
    db_group = models.CharacterGroup(**group.dict())
    db.add(db_group)
    db.commit()
    db.refresh(db_group)
    return db_group

@app.get("/groups/", response_model=List[schemas.CharacterGroup])
def read_groups(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    groups = db.query(models.CharacterGroup).offset(skip).limit(limit).all()
    return groups

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)