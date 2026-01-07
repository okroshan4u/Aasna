import uuid
import random
from datetime import datetime, timedelta


PROJECT_TEMPLATES = {
    "product": [
        "Core Platform Improvements",
        "Authentication Refactor",
        "Mobile App Enhancements",
        "API Reliability Upgrade",
        "Developer Experience Initiative",
        "Performance Optimization Sprint",
    ],
    "marketing": [
        "Q{q} Brand Campaign",
        "Product Launch Enablement",
        "Growth Experiments Cycle",
        "Content Marketing Roadmap",
        "SEO & Organic Growth",
    ],
    "operations": [
        "Internal Process Optimization",
        "Customer Support Scaling",
        "Billing & Finance Operations",
        "Compliance Readiness Program",
        "Vendor Management Initiative",
        "IT Infrastructure Maintenance",
    ],
}


def generate_projects(conn, organization_id):
    """
    Generate realistic team-scoped projects.
    """

    cursor = conn.cursor()

    teams = cursor.execute(
        "SELECT team_id, team_type FROM teams"
    ).fetchall()

    projects = []

    for team_id, team_type in teams:
        if team_type == "product":
            count = 20
        elif team_type == "marketing":
            count = 15
        else:
            count = 25

        templates = PROJECT_TEMPLATES[team_type]

        for i in range(count):
            project_id = str(uuid.uuid4())

            base_name = random.choice(templates)
            if "{q}" in base_name:
                base_name = base_name.format(q=random.randint(1, 4))

            status = random.choices(
                ["planned", "active", "completed"],
                weights=[0.25, 0.5, 0.25],
            )[0]

            start_date = datetime.now() - timedelta(
                days=random.randint(0, 180)
            )

            due_date = start_date + timedelta(
                days=random.randint(30, 180)
            )

            projects.append(
                (
                    project_id,
                    team_id,
                    base_name,
                    team_type,
                    status,
                    start_date.date().isoformat(),
                    due_date.date().isoformat(),
                    datetime.now().isoformat(),
                )
            )

    cursor.executemany(
        """
        INSERT INTO projects
        (project_id, team_id, name, project_type, status, start_date, due_date, created_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """,
        projects
    )

    conn.commit()
