import uuid

def generate_teams(conn, org_id):
    teams = [
        (str(uuid.uuid4()), org_id, "Product", "product"),
        (str(uuid.uuid4()), org_id, "Marketing", "marketing"),
        (str(uuid.uuid4()), org_id, "Operations", "operations")
    ]

    conn.executemany("""
        INSERT INTO teams VALUES (?, ?, ?, ?, CURRENT_TIMESTAMP)
    """, teams)

    return [t[0] for t in teams]
