from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Dict, Any
from ..schemas.character import CharacterRelationshipCreateSchema, CharacterCreateSchema, CharacterSchema, RelatedCharacterSchema
from ..models.character import Character
from ..database import get_db

router = APIRouter(
    prefix="/characters",
    tags=["characters"]
)

def format_character(character: Character, expand: List[str]) -> Dict[str, Any]:
    """Format a character with optional relationship expansion"""

    char_dict = {
        "id": character.id,
        "name": character.name,
        "actor_name": character.actor_name,
        "character_type": character.character_type,
        "description": character.description,
        "relationships": []
    }

    print(f"Will format character with expand:{expand}")
    
    # Expand relationships if needed
    if "relationships" in expand:
        # Use the ORM relationships
        for rel in character.outgoing_relationships:
            related_character = rel.related_character
            char_dict["relationships"].append({
                "id": related_character.id,
                "name": related_character.name,
                "relationship_type": rel.relationship_type
            })
    
    return char_dict


@router.post("/", response_model=CharacterSchema)
def create_character(character: CharacterCreateSchema, db: Session = Depends(get_db)):
    db_character = Character(**character.model_dump())
    db.add(db_character)
    db.commit()
    db.refresh(db_character)
    return db_character

@router.get("/", response_model=List[CharacterSchema])
def read_characters(skip: int = 0, limit: int = 100, expand: List[str] = Query(default=[]), db: Session = Depends(get_db)):
    characters = db.query(Character).offset(skip).limit(limit).all()
    return [format_character(character=character, expand=expand) for character in characters]

@router.post("/{character_id}/relationships", response_model=CharacterSchema)
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
def read_character(character_id: str, expand: List[str] = Query(default=[]), db: Session = Depends(get_db)):
    db_character = db.query(Character).filter(Character.id == character_id).first()
    if db_character is None:
        raise HTTPException(status_code=404, detail="Character not found")
    return format_character(character=db_character, expand=expand)