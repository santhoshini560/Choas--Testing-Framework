import random

def simulate_network_failure():
    """
    Simulates network behavior for chaos testing.
    Sometimes runs normally, sometimes fails with different issues.
    """

    outcomes = [
        "Network Connected",
        "Network Timeout",
        "Connection Refused",
        "Packet Loss Detected",
        "High Latency"
    ]

    result = random.choice(outcomes)

    if result == "Network Connected":
        return result
    else:
        # Raise exception to mimic network failure
        raise Exception(result)


# Testing
if __name__ == "__main__":
    print("===== NETWORK FAILURE TEST =====")
    try:
        print(simulate_network_failure())
    except Exception as e:
        print("Network Failure Triggered:", e)
