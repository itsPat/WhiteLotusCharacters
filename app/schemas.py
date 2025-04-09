
from pydantic import BaseModel
from typing import List, Optional

class CharacterBase(BaseModel):
    name: str
    actor_name: str
    character_type: str
    description: Optional[str] = None
    group_id: Optional[str] = None

class CharacterCreate(CharacterBase):
    pass

class CharacterRelationshipCreate(BaseModel):
    related_character_id: str
    relationship_type: str

class Character(CharacterBase):
    id: str
    relationships: List["RelatedCharacter"] = []
    
    class Config:
        from_attributes = True

class RelatedCharacter(BaseModel):
    id: str
    name: str
    relationship_type: str
    
    class Config:
        from_attributes = True

class CharacterGroupBase(BaseModel):
    name: str
    description: Optional[str] = None

class CharacterGroupCreate(CharacterGroupBase):
    pass

class CharacterGroup(CharacterGroupBase):
    id: str
    characters: List[Character] = []
    
    class Config:
        from_attributes = True