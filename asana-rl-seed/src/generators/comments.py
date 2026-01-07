import uuid
from faker import Faker

fake = Faker()

def generate_comments(conn, task_ids, user_ids):
    comments = []
    for task in task_ids:
        for _ in range(fake.random_int(0, 5)):
            comments.append((
                str(uuid.uuid4()),
                task,
                fake.random_element(user_ids),
                fake.sentence(),
                fake.date_time_this_year()
            ))

    conn.executemany("""
        INSERT INTO comments VALUES (?, ?, ?, ?, ?)
    """, comments)
