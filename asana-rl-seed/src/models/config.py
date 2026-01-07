"""
Central configuration for the Asana RL seed data generator.

All tunable parameters (scale, dates, probabilities) are defined here
to ensure reproducibility, clarity, and easy experimentation.
"""

import os
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables from .env if present
load_dotenv()

# -----------------------------
# Database Configuration
# -----------------------------

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
OUTPUT_DIR = os.path.join(BASE_DIR, "output")

DB_NAME = "asana_simulation.sqlite"
DB_PATH = os.path.join(OUTPUT_DIR, DB_NAME)

# -----------------------------
# Organization Configuration
# -----------------------------

ORGANIZATION_ID = "org_1"
ORGANIZATION_NAME = "Example SaaS Corporation"
ORGANIZATION_DOMAIN = "example.com"

# -----------------------------
# Scale Configuration
# -----------------------------

NUM_USERS = int(os.getenv("NUM_USERS", 7000))
NUM_PROJECTS = int(os.getenv("NUM_PROJECTS", 120))

# -----------------------------
# Temporal Configuration
# -----------------------------

START_DATE = datetime.fromisoformat(
    os.getenv("START_DATE", "2025-07-01")
)

END_DATE = datetime.fromisoformat(
    os.getenv("END_DATE", "2026-01-01")
)

# -----------------------------
# Team Configuration
# -----------------------------

TEAM_TYPES = {
    "product": {
        "name": "Product Engineering",
        "project_types": ["sprint", "platform", "bug-tracking"]
    },
    "marketing": {
        "name": "Marketing",
        "project_types": ["campaign", "launch", "content"]
    },
    "operations": {
        "name": "Operations",
        "project_types": ["process", "support", "compliance"]
    }
}

# -----------------------------
# Task Generation Parameters
# -----------------------------

TASKS_PER_PROJECT_RANGE = (40, 120)
SUBTASK_PROBABILITY = 0.35
UNASSIGNED_TASK_PROBABILITY = 0.15

PRIORITY_DISTRIBUTION = {
    "low": 0.25,
    "medium": 0.50,
    "high": 0.25
}

# Completion likelihood by project type
COMPLETION_RATES = {
    "sprint": (0.70, 0.85),
    "bug-tracking": (0.60, 0.70),
    "platform": (0.50, 0.65),
    "campaign": (0.60, 0.75),
    "operations": (0.40, 0.55)
}

# -----------------------------
# Due Date Distribution
# -----------------------------

DUE_DATE_DISTRIBUTION = {
    "within_1_week": 0.25,
    "within_1_month": 0.40,
    "within_3_months": 0.20,
    "no_due_date": 0.10,
    "overdue": 0.05
}

AVOID_WEEKENDS_PROBABILITY = 0.85

# -----------------------------
# Comment Generation
# -----------------------------

COMMENTS_PER_TASK_RANGE = (0, 5)

# -----------------------------
# Tag Configuration
# -----------------------------

DEFAULT_TAGS = [
    "frontend",
    "backend",
    "infrastructure",
    "security",
    "urgent",
    "tech-debt",
    "customer-facing"
]

# -----------------------------
# LLM Configuration (Optional)
# -----------------------------

USE_LLM = os.getenv("USE_LLM", "false").lower() == "true"
LLM_PROVIDER = os.getenv("LLM_PROVIDER", "openai")
LLM_MODEL = os.getenv("LLM_MODEL", "gpt-4o-mini")
LLM_TEMPERATURE = float(os.getenv("LLM_TEMPERATURE", 0.7))

# -----------------------------
# Safety / Validation
# -----------------------------

def validate_config():
    assert NUM_USERS > 0, "NUM_USERS must be positive"
    assert NUM_PROJECTS > 0, "NUM_PROJECTS must be positive"
    assert START_DATE < END_DATE, "START_DATE must be before END_DATE"


validate_config()
