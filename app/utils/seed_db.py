from sqlalchemy.orm import Session
from ..models.character import Character, CharacterRelationship
from ..database import get_db

def seed_characters(db: Session):
    # Check if database is already seeded
    if db.query(Character).count() > 0:
        return
    
    # Create characters
    characters = [
        # The Ratliff Family
        Character(
            name="Timothy Ratliff",
            actor_name="Jason Isaacs",
            character_type="guest",
            description="A financier in jeopardy from Durham, North Carolina"
        ),
        Character(
            name="Victoria Ratliff",
            actor_name="Parker Posey",
            character_type="guest",
            description="Timothy's wife and mother to Saxon, Piper, and Lochlan"
        ),
        Character(
            name="Saxon Ratliff",
            actor_name="Patrick Schwarzenegger",
            character_type="guest",
            description="Timothy and Victoria's oldest child, who works for his father's company"
        ),
        Character(
            name="Piper Ratliff",
            actor_name="Sarah Catherine Hook",
            character_type="guest",
            description="A college senior studying religion and middle child of Timothy and Victoria"
        ),
        Character(
            name="Lochlan Ratliff",
            actor_name="Sam Nivola",
            character_type="guest",
            description="A shy high school senior and Timothy and Victoria's youngest child"
        ),
        
        # The Friends Group
        Character(
            name="Kate Bohr",
            actor_name="Leslie Bibb",
            character_type="guest",
            description="A country club wife from Austin, Texas, one of three longtime friends reuniting on a girls' trip"
        ),
        Character(
            name="Laurie Duffy",
            actor_name="Carrie Coon",
            character_type="guest",
            description="A corporate lawyer and recent divorcée from New York City, one of three longtime friends reuniting on a girls' trip"
        ),
        Character(
            name="Jaclyn Lemon",
            actor_name="Michelle Monaghan",
            character_type="guest",
            description="A successful television actress based in Hollywood, one of three longtime friends reuniting on a girls' trip"
        ),
        
        # The Couple
        Character(
            name="Rick Hatchett",
            actor_name="Walton Goggins",
            character_type="guest",
            description="A rugged and mysterious man with a chip on his shoulder, traveling with his young girlfriend Chelsea"
        ),
        Character(
            name="Chelsea",
            actor_name="Aimee Lou Wood",
            character_type="guest",
            description="A free spirit from Manchester traveling with Rick, her much older boyfriend"
        ),
        
        # Hotel Staff
        Character(
            name="Belinda Lindsey",
            actor_name="Natasha Rothwell",
            character_type="staff",
            description="A spa manager from the White Lotus in Hawaii, attending a work exchange"
        ),
        Character(
            name="Thidapon 'Mook' Sornsin",
            actor_name="Lalisa Manobal",
            character_type="staff",
            description="A health mentor for guests of the White Lotus"
        ),
        Character(
            name="Gaitok",
            actor_name="Tayme Thapthimthong",
            character_type="staff",
            description="A security guard at the White Lotus"
        ),
        
        # Hotel Owners
        Character(
            name="Sritala Hollinger",
            actor_name="Lek Patravadi",
            character_type="owner",
            description="One of the owners of the White Lotus, who pioneered its health program"
        ),
        Character(
            name="Jim Hollinger",
            actor_name="Scott Glenn",
            character_type="owner",
            description="Sritala's American husband who has recently suffered a stroke"
        ),
        
        # Others
        Character(
            name="Greg Hunt",
            actor_name="Jon Gries",
            character_type="guest",
            description="A man involved with Chloe and the widower of Tanya McQuoid"
        ),
        Character(
            name="Frank",
            actor_name="Sam Rockwell",
            character_type="guest",
            description="Rick's friend and former associate"
        )
    ]
    
    # Add all characters to the database
    db.add_all(characters)
    db.commit()
    
    # Refresh to get IDs
    for character in characters:
        db.refresh(character)
    
    return characters

def seed_relationships(db: Session, characters: list[Character]):
    # Get characters by name for easier reference
    char_dict = {character.name: character for character in characters}
    
    # Define a function to create relationships with types
    def add_relationship(char1, char2, rel_type):
        relationship = CharacterRelationship(
            character_id=char1.id,
            related_character_id=char2.id,
            relationship_type=rel_type
        )
        db.add(relationship)
    
    # Ratliff family
    add_relationship(char_dict["Timothy Ratliff"], char_dict["Victoria Ratliff"], "Spouse")
    add_relationship(char_dict["Victoria Ratliff"], char_dict["Timothy Ratliff"], "Spouse")
    
    # Parents-children
    for child_name in ["Saxon Ratliff", "Piper Ratliff", "Lochlan Ratliff"]:
        add_relationship(char_dict["Timothy Ratliff"], char_dict[child_name], "Parent")
        add_relationship(char_dict["Victoria Ratliff"], char_dict[child_name], "Parent")
        add_relationship(char_dict[child_name], char_dict["Timothy Ratliff"], "Child")
        add_relationship(char_dict[child_name], char_dict["Victoria Ratliff"], "Child")
    
    # Rest of your relationships...
    
    # Fix the "Mook" reference using the full name
    add_relationship(char_dict["Thidapon 'Mook' Sornsin"], char_dict["Gaitok"], "Flirt")
    add_relationship(char_dict["Gaitok"], char_dict["Thidapon 'Mook' Sornsin"], "Flirt")
    
    db.commit()

def seed_db():
    print("Starting database seeding...")
    # Get a database session
    db = next(get_db())
    print("Database connection obtained")
    
    # Populate characters
    characters = seed_characters(db)
    print(f"Characters seeded: {characters is not None}")
    
    # Create relationships if characters were just created
    if characters:
        seed_relationships(db, characters)
        print("Relationships seeded")
    
    db.close()
    print("Database seeding completed")