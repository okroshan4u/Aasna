import uuid

def generate_tags(conn):
    tags = ["security", "frontend", "backend", "infra", "urgent"]
    tag_ids = []

    for t in tags:
        tid = str(uuid.uuid4())
        tag_ids.append(tid)
        conn.execute("INSERT INTO tags VALUES (?, ?)", (tid, t))

    return tag_ids
