from database.mongodb import db
import random

def simulate_attack():

    attack_types = [
        {
            "eventType": "Brute Force Attempt",
            "severity": "High"
        },
        {
            "eventType": "Suspicious IAM Activity",
            "severity": "High"
        },
        {
            "eventType": "Unusual Access Location",
            "severity": "Critical"
        },
        {
            "eventType": "Multiple Failed Logins",
            "severity": "Medium"
        }
    ]

    attack = random.choice(attack_types)

    attack["sourceIP"] = f"192.168.1.{random.randint(1,255)}"
    attack["status"] = "Open"

    result = db.security_events.insert_one(attack)

    return {
        "message": "Attack simulated successfully",
        "eventId": str(result.inserted_id)
    }