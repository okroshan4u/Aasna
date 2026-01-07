import numpy as np

def due_date_offset():
    r = np.random.rand()
    if r < 0.25:
        return np.random.randint(1, 7)
    elif r < 0.65:
        return np.random.randint(7, 30)
    elif r < 0.85:
        return np.random.randint(30, 90)
    elif r < 0.95:
        return None   # no due date
    else:
        return -np.random.randint(1, 30)  # overdue
