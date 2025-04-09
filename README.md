![White Lotus Cast](/public/white_lotus_cast.jpg)

# White Lotus Characters

> This FastAPI application models the relationships between characters on White Lotus Season 3.

---

# Setup Instructions

## Prerequisites

- Python 3.11 or higher
- PostgreSQL 14 or higher

## Step 1: Setup virtual environment

```bash
python -m venv venv
# On MacOS
source venv/bin/activate
```

## Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

## Step 3: Set up PostgreSQL

```bash
brew services start postgresql

# Create a database
createdb white_lotus_characters_db
```

## Step 4: Run the application

```bash
python -m app.main
```

The API will be available at http://127.0.0.1:8000
You can access the documentation at http://127.0.0.1:8000/docs

## Step 4: Test your implementation

```
curl --location 'http://127.0.0.1:8000/characters?expand=relationships' \
--header 'accept: application/json'
```

```json
[
  {
    "name": "Timothy Ratliff",
    "actor_name": "Jason Isaacs",
    "character_type": "guest",
    "description": "A financier in jeopardy from Durham, North Carolina",
    "id": "aa860e2a-5291-471c-a463-d8a326e2364d",
    "relationships": [
      {
        "id": "34ad9305-bd9f-4b90-8c7f-368af33731d5",
        "name": "Victoria Ratliff",
        "relationship_type": "Spouse"
      },
      {
        "id": "9604a8b2-ce48-4d36-a4f1-dafe8931313b",
        "name": "Saxon Ratliff",
        "relationship_type": "Parent"
      },
      {
        "id": "fcbd1ee4-8f5d-47b2-b17f-d3d70de37865",
        "name": "Piper Ratliff",
        "relationship_type": "Parent"
      },
      {
        "id": "cecea011-10f0-4ec3-b2df-5fc5a48342ef",
        "name": "Lochlan Ratliff",
        "relationship_type": "Parent"
      }
    ]
  },
  {
    "name": "Victoria Ratliff",
    "actor_name": "Parker Posey",
    "character_type": "guest",
    "description": "Timothy's wife and mother to Saxon, Piper, and Lochlan",
    "id": "34ad9305-bd9f-4b90-8c7f-368af33731d5",
    "relationships": [
      {
        "id": "aa860e2a-5291-471c-a463-d8a326e2364d",
        "name": "Timothy Ratliff",
        "relationship_type": "Spouse"
      },
      {
        "id": "9604a8b2-ce48-4d36-a4f1-dafe8931313b",
        "name": "Saxon Ratliff",
        "relationship_type": "Parent"
      },
      {
        "id": "fcbd1ee4-8f5d-47b2-b17f-d3d70de37865",
        "name": "Piper Ratliff",
        "relationship_type": "Parent"
      },
      {
        "id": "cecea011-10f0-4ec3-b2df-5fc5a48342ef",
        "name": "Lochlan Ratliff",
        "relationship_type": "Parent"
      }
    ]
  },
  {
    "name": "Saxon Ratliff",
    "actor_name": "Patrick Schwarzenegger",
    "character_type": "guest",
    "description": "Timothy and Victoria's oldest child, who works for his father's company",
    "id": "9604a8b2-ce48-4d36-a4f1-dafe8931313b",
    "relationships": [
      {
        "id": "aa860e2a-5291-471c-a463-d8a326e2364d",
        "name": "Timothy Ratliff",
        "relationship_type": "Child"
      },
      {
        "id": "34ad9305-bd9f-4b90-8c7f-368af33731d5",
        "name": "Victoria Ratliff",
        "relationship_type": "Child"
      }
    ]
  },
  {
    "name": "Piper Ratliff",
    "actor_name": "Sarah Catherine Hook",
    "character_type": "guest",
    "description": "A college senior studying religion and middle child of Timothy and Victoria",
    "id": "fcbd1ee4-8f5d-47b2-b17f-d3d70de37865",
    "relationships": [
      {
        "id": "aa860e2a-5291-471c-a463-d8a326e2364d",
        "name": "Timothy Ratliff",
        "relationship_type": "Child"
      },
      {
        "id": "34ad9305-bd9f-4b90-8c7f-368af33731d5",
        "name": "Victoria Ratliff",
        "relationship_type": "Child"
      }
    ]
  },
  {
    "name": "Lochlan Ratliff",
    "actor_name": "Sam Nivola",
    "character_type": "guest",
    "description": "A shy high school senior and Timothy and Victoria's youngest child",
    "id": "cecea011-10f0-4ec3-b2df-5fc5a48342ef",
    "relationships": [
      {
        "id": "aa860e2a-5291-471c-a463-d8a326e2364d",
        "name": "Timothy Ratliff",
        "relationship_type": "Child"
      },
      {
        "id": "34ad9305-bd9f-4b90-8c7f-368af33731d5",
        "name": "Victoria Ratliff",
        "relationship_type": "Child"
      }
    ]
  },
  {
    "name": "Kate Bohr",
    "actor_name": "Leslie Bibb",
    "character_type": "guest",
    "description": "A country club wife from Austin, Texas, one of three longtime friends reuniting on a girls' trip",
    "id": "d5252814-76aa-488e-a77e-8236b9423963",
    "relationships": []
  },
  {
    "name": "Laurie Duffy",
    "actor_name": "Carrie Coon",
    "character_type": "guest",
    "description": "A corporate lawyer and recent divorcée from New York City, one of three longtime friends reuniting on a girls' trip",
    "id": "f635c1a4-20ac-4e4b-8b96-18f5a95f6ecc",
    "relationships": []
  },
  {
    "name": "Jaclyn Lemon",
    "actor_name": "Michelle Monaghan",
    "character_type": "guest",
    "description": "A successful television actress based in Hollywood, one of three longtime friends reuniting on a girls' trip",
    "id": "276354db-2206-427b-80db-a8dc46d65661",
    "relationships": []
  },
  {
    "name": "Rick Hatchett",
    "actor_name": "Walton Goggins",
    "character_type": "guest",
    "description": "A rugged and mysterious man with a chip on his shoulder, traveling with his young girlfriend Chelsea",
    "id": "725fbed1-0d64-4a3e-8803-cf6857f9943c",
    "relationships": []
  },
  {
    "name": "Chelsea",
    "actor_name": "Aimee Lou Wood",
    "character_type": "guest",
    "description": "A free spirit from Manchester traveling with Rick, her much older boyfriend",
    "id": "104810e9-e812-461e-a006-a7865e9c9ef3",
    "relationships": []
  },
  {
    "name": "Belinda Lindsey",
    "actor_name": "Natasha Rothwell",
    "character_type": "staff",
    "description": "A spa manager from the White Lotus in Hawaii, attending a work exchange",
    "id": "0331119a-2134-4452-800e-50a218808891",
    "relationships": []
  },
  {
    "name": "Thidapon 'Mook' Sornsin",
    "actor_name": "Lalisa Manobal",
    "character_type": "staff",
    "description": "A health mentor for guests of the White Lotus",
    "id": "4ed6dec0-07fb-4101-8167-0010490c98e6",
    "relationships": [
      {
        "id": "0588d8d8-3329-4c4c-9bce-de0fc8a85087",
        "name": "Gaitok",
        "relationship_type": "Flirt"
      }
    ]
  },
  {
    "name": "Gaitok",
    "actor_name": "Tayme Thapthimthong",
    "character_type": "staff",
    "description": "A security guard at the White Lotus",
    "id": "0588d8d8-3329-4c4c-9bce-de0fc8a85087",
    "relationships": [
      {
        "id": "4ed6dec0-07fb-4101-8167-0010490c98e6",
        "name": "Thidapon 'Mook' Sornsin",
        "relationship_type": "Flirt"
      }
    ]
  },
  {
    "name": "Sritala Hollinger",
    "actor_name": "Lek Patravadi",
    "character_type": "owner",
    "description": "One of the owners of the White Lotus, who pioneered its health program",
    "id": "97796dbe-48b9-4dc9-8bf2-d739c4e29ee4",
    "relationships": []
  },
  {
    "name": "Jim Hollinger",
    "actor_name": "Scott Glenn",
    "character_type": "owner",
    "description": "Sritala's American husband who has recently suffered a stroke",
    "id": "d93c4eb1-3625-4d44-a50a-4d70df666fe0",
    "relationships": []
  },
  {
    "name": "Greg Hunt",
    "actor_name": "Jon Gries",
    "character_type": "guest",
    "description": "A man involved with Chloe and the widower of Tanya McQuoid",
    "id": "bcdc6d61-0680-4ace-bfcf-5943566e50f7",
    "relationships": []
  },
  {
    "name": "Frank",
    "actor_name": "Sam Rockwell",
    "character_type": "guest",
    "description": "Rick's friend and former associate",
    "id": "0b1cda00-5bad-4519-a18e-99e67572a256",
    "relationships": []
  }
]
```

---
