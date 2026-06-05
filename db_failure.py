import random

def simulate_db_failure():
    """
    Simulates database behavior for chaos testing.
    Sometimes runs normally, sometimes fails with different issues.
    """

    outcomes = [
        "Database Running",
        "Database Connection Lost",
        "Database Crash",
        "Database Timeout",
        "Database Corruption Detected"
    ]

    result = random.choice(outcomes)

    if result == "Database Running":
        return result
    else:
        # Raise exception to mimic failure
        raise Exception(result)


# Testing
if __name__ == "__main__":
    print("===== DATABASE FAILURE TEST =====")
    try:
        print(simulate_db_failure())
    except Exception as e:
        print("Database Failure Triggered:", e)
