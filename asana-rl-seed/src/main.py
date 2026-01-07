import sqlite3
from pathlib import Path

# -----------------------------
# Resolve project root safely
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
SCHEMA_PATH = BASE_DIR / "schema.sql"
DB_PATH = BASE_DIR / "output" / "asana_simulation.sqlite"

# Ensure output directory exists
DB_PATH.parent.mkdir(exist_ok=True)

# -----------------------------
# Initialize database
# -----------------------------
conn = sqlite3.connect(DB_PATH)

with open(SCHEMA_PATH, "r", encoding="utf-8") as f:
    conn.executescript(f.read())

conn.commit()
conn.close()

print("Database schema initialized successfully.")

