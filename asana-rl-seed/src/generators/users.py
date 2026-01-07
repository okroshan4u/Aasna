import uuid
import random
from datetime import datetime, timedelta

from faker import Faker

fake = Faker()


def generate_users(conn, organization_id, num_users):
    """
    Generate realistic users for an Asana workspace.

    - Unique company-domain emails
    - ~5% admins, ~95% members
    - ~95% active users
    - Join dates spread over last 24 months
    """

    cursor = conn.cursor()
    users = []

    for _ in range(num_users):
        user_id = str(uuid.uuid4())
        full_name = fake.name()

        email_prefix = full_name.lower().replace(" ", ".")
        email_suffix = user_id[:6]
        email = f"{email_prefix}.{email_suffix}@example.com"

        role = "admin" if random.random() < 0.05 else "member"
        is_active = 1 if random.random() < 0.95 else 0

        joined_at = datetime.now() - timedelta(
            days=random.randint(0, 730)
        )

        users.append(
            (
                user_id,
                organization_id,
                full_name,
                email,
                role,
                is_active,
                joined_at.isoformat()
            )
        )

    cursor.executemany(
        """
        INSERT INTO users
        (user_id, organization_id, full_name, email, role, is_active, joined_at)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        users
    )

    conn.commit()
