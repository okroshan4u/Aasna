import uuid
import random
from datetime import datetime, timedelta
from utils.distributions import due_date_offset

def generate_tasks(conn, project_ids, user_ids):
    tasks = []

    for project_id in project_ids:
        for _ in range(random.randint(40, 120)):
            tid = str(uuid.uuid4())
            assignee = random.choice(user_ids) if random.random() > 0.15 else None

            offset = due_date_offset()
            due = None
            if offset is not None:
                due = datetime.now() + timedelta(days=offset)

            completed = random.random() < 0.7

            tasks.append((
                tid,
                project_id,
                None,
                assignee,
                f"Task {tid[:8]} – Implement feature",
                "Detailed task description",
                due,
                random.choice(["low", "medium", "high"]),
                int(completed),
                datetime.now(),
                datetime.now() if completed else None
            ))

    conn.executemany("""
        INSERT INTO tasks VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, tasks)
