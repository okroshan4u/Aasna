import sqlite3
from pathlib import Path
from generators.users import generate_users
from models.config import NUM_USERS
from generators.teams import generate_teams
from generators.projects import generate_projects



from models.config import (
    ORGANIZATION_ID,
    ORGANIZATION_NAME,
    ORGANIZATION_DOMAIN
)

# -----------------------------
# Resolve project root safely
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
SCHEMA_PATH = BASE_DIR / "schema.sql"
DB_PATH = BASE_DIR / "output" / "asana_simulation.sqlite"

DB_PATH.parent.mkdir(exist_ok=True)

# -----------------------------
# Connect to database
# -----------------------------
conn = sqlite3.connect(DB_PATH)
conn.execute("PRAGMA foreign_keys = ON;")

# -----------------------------
# Initialize schema
# -----------------------------
with open(SCHEMA_PATH, "r", encoding="utf-8") as f:
    conn.executescript(f.read())

print("Database schema initialized successfully.")

# -----------------------------
# Insert organization (STEP 1)
# -----------------------------
conn.execute(
    """
    INSERT OR IGNORE INTO organizations
    (organization_id, name, domain, created_at)
    VALUES (?, ?, ?, CURRENT_TIMESTAMP)
    """,
    (ORGANIZATION_ID, ORGANIZATION_NAME, ORGANIZATION_DOMAIN)
)

print("Organization inserted successfully.")

# -----------------------------
# STEP 2: Generate users
# -----------------------------
print(f"Generating {NUM_USERS} users...")
generate_users(conn, ORGANIZATION_ID, NUM_USERS)

# conn.close()
print("Users generated successfully.")

# -----------------------------
# STEP 3: Generate teams & memberships
# -----------------------------
print("Generating teams and team memberships...")
generate_teams(conn, ORGANIZATION_ID)
print("Teams and memberships generated successfully.")

# -----------------------------
# STEP 4: Generate projects
# -----------------------------
print("Generating projects...")
generate_projects(conn, ORGANIZATION_ID)
print("Projects generated successfully.")



