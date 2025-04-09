from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..schemas.character import CharacterRelationshipCreateSchema, CharacterCreateSchema, CharacterSchema, RelatedCharacterSchema
from ..models.character import Character
from ..database import get_db

router = APIRouter(
    prefix="/characters",
    tags=["characters"]
)

@router.post("/", response_model=CharacterSchema)
def create_character(character: CharacterCreateSchema, db: Session = Depends(get_db)):
    db_character = Character(**character.model_dump())
    db.add(db_character)
    db.commit()
    db.refresh(db_character)
    return db_character

@router.get("/", response_model=List[CharacterSchema])
def read_characters(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    characters = db.query(Character).offset(skip).limit(limit).all()
    return characters

@router.post("/{character_id}/relationships/", response_model=CharacterSchema)
def create_relationship(
    character_id: str, 
    relationship: CharacterRelationshipCreateSchema, 
    db: Session = Depends(get_db)
):
    db_character = db.query(Character).filter(Character.id == character_id).first()
    if not db_character:
        raise HTTPException(status_code=404, detail="Character not found")
    
    related_character = db.query(Character).filter(
        Character.id == relationship.related_character_id
    ).first()
    if not related_character:
        raise HTTPException(status_code=404, detail="Related character not found")
    
    # Add relationship
    db_character.relationships.append(related_character)
    db.commit()
    db.refresh(db_character)
    return db_character

@router.get("/{character_id}", response_model=CharacterSchema)
def read_character(character_id: str, db: Session = Depends(get_db)):
    db_character = db.query(Character).filter(Character.id == character_id).first()
    if db_character is None:
        raise HTTPException(status_code=404, detail="Character not found")
    return db_character