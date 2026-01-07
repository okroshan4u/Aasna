import uuid
import random
from datetime import datetime


def generate_teams(conn, organization_id):
    """
    Generate core teams for the organization and assign users to them.

    Returns
    -------
    list[str]
        List of team IDs
    """

    cursor = conn.cursor()

    teams = [
        ("Product", "product"),
        ("Marketing", "marketing"),
        ("Operations", "operations"),
    ]

    team_ids = {}

    # Insert teams
    for name, team_type in teams:
        team_id = str(uuid.uuid4())
        team_ids[team_type] = team_id

        cursor.execute(
            """
            INSERT INTO teams
            (team_id, organization_id, name, team_type, created_at)
            VALUES (?, ?, ?, ?, CURRENT_TIMESTAMP)
            """,
            (team_id, organization_id, name, team_type)
        )

    conn.commit()

    # Fetch users
    user_ids = [
        row[0]
        for row in cursor.execute("SELECT user_id FROM users").fetchall()
    ]

    # Assign users to teams
    memberships = []

    for user_id in user_ids:
        r = random.random()

        if r < 0.65:
            assigned = [team_ids["operations"]]
        elif r < 0.85:
            assigned = [team_ids["product"]]
        elif r < 0.95:
            assigned = [team_ids["marketing"]]
        else:
            assigned = list(team_ids.values())  # cross-functional

        for team_id in assigned:
            memberships.append(
                (team_id, user_id, datetime.now().isoformat())
            )

    cursor.executemany(
        """
        INSERT INTO team_memberships
        (team_id, user_id, joined_at)
        VALUES (?, ?, ?)
        """,
        memberships
    )

    conn.commit()

    return list(team_ids.values())
