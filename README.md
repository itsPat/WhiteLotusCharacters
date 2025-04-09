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
createdb fastapi_db
```

## Step 4: Run the application

```bash
python -m app.main
```

The API will be available at http://127.0.0.1:8000
You can access the documentation at http://127.0.0.1:8000/docs

---
