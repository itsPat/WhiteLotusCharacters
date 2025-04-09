from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base
import uuid

def generate_uuid():
    return str(uuid.uuid4())

class CharacterRelationship(Base):
    __tablename__ = "character_relationships"
    
    character_id = Column(String, ForeignKey("characters.id"), primary_key=True)
    related_character_id = Column(String, ForeignKey("characters.id"), primary_key=True)
    relationship_type = Column(String, nullable=False)  # Make this non-nullable
    
    # References to the actual characters
    character = relationship("Character", foreign_keys=[character_id], back_populates="outgoing_relationships")
    related_character = relationship("Character", foreign_keys=[related_character_id], back_populates="incoming_relationships")

class Character(Base):
    __tablename__ = "characters"
    
    id = Column(String, primary_key=True, index=True, default=generate_uuid)
    name = Column(String, index=True)
    actor_name = Column(String)
    character_type = Column(String)  # guest, staff, etc.
    description = Column(String)
    
    # Relationships in both directions
    outgoing_relationships = relationship("CharacterRelationship", foreign_keys=[CharacterRelationship.character_id], back_populates="character")
    incoming_relationships = relationship("CharacterRelationship", foreign_keys=[CharacterRelationship.related_character_id], back_populates="related_character")