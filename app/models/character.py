from sqlalchemy import Column, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from .base import Base
import uuid

def generate_uuid():
    return str(uuid.uuid4())

# Association table for many-to-many relationships
character_relationships = Table(
    "character_relationships",
    Base.metadata,
    Column("character_id", String, ForeignKey("characters.id"), primary_key=True),
    Column("related_character_id", String, ForeignKey("characters.id"), primary_key=True),
    Column("relationship_type", String),
)

class Character(Base):
    __tablename__ = "characters"
    
    id = Column(String, primary_key=True, index=True, default=generate_uuid)
    name = Column(String, index=True)
    actor_name = Column(String)
    character_type = Column(String)  # guest, staff, etc.
    description = Column(String)
    
    # Self-referential relationship
    relationships = relationship(
        "Character",
        secondary=character_relationships,
        primaryjoin=(character_relationships.c.character_id == id),
        secondaryjoin=(character_relationships.c.related_character_id == id),
        backref="related_to"
    )