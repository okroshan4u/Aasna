import uuid
import random

PROJECT_TYPES = {
    "product": ["Sprint", "Platform", "Bug Tracking"],
    "marketing": ["Campaign", "Launch", "Content"],
    "operations": ["Process", "Support", "Compliance"]
}

def generate_projects(conn, team_ids):
    projects = []

    for team_id in team_ids:
        for _ in range(random.randint(20, 40)):
            pid = str(uuid.uuid4())
            projects.append((
                pid,
                team_id,
                f"Project {pid[:6]}",
                random.choice(sum(PROJECT_TYPES.values(), [])),
                "active",
                None,
                None,
            ))

    conn.executemany("""
        INSERT INTO projects VALUES (?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
    """, projects)

    return [p[0] for p in projects]
