from pydantic import BaseModel
from typing import List, Optional

class CharacterBaseSchema(BaseModel):
    name: str
    actor_name: str
    character_type: str
    description: Optional[str] = None

class CharacterCreateSchema(CharacterBaseSchema):
    pass

class CharacterRelationshipCreateSchema(BaseModel):
    related_character_id: str
    relationship_type: str

class RelatedCharacterSchema(BaseModel):
    id: str
    name: str
    relationship_type: str
    
    class Config:
        from_attributes = True

class CharacterSchema(CharacterBaseSchema):
    id: str
    relationships: List[RelatedCharacterSchema] = []
    
    class Config:
        from_attributes = True
