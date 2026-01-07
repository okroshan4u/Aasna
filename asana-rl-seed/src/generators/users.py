from faker import Faker
import uuid
import random

fake = Faker()

def generate_users(conn, org_id, n):
    users = []
    for _ in range(n):
        uid = str(uuid.uuid4())
        users.append((
            uid,
            org_id,
            fake.name(),
            fake.email(),
            random.choice(["admin", "member"]),
            1,
            fake.date_time_this_year()
        ))

    conn.executemany("""
        INSERT INTO users VALUES (?, ?, ?, ?, ?, ?, ?)
    """, users)
