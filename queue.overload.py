import random

def simulate_queue_overload():
    """
    Simulates request queue behavior for chaos testing.
    Sometimes healthy, sometimes overloaded.
    """

    requests = random.randint(50, 1000)

    if requests < 500:
        return f"Queue Healthy - {requests} requests"
    else:
        # Raise exception to mimic overload condition
        raise Exception(f"Queue Overloaded - {requests} requests")


# Testing
if __name__ == "__main__":
    print("===== QUEUE OVERLOAD TEST =====")
    try:
        print(simulate_queue_overload())
    except Exception as e:
        print("Queue Failure Triggered:", e)
