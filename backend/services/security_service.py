from database.mongodb import db

def get_security_events():

    events = list(
        db.security_events.find({}, {"_id": 0})
    )

    for event in events:

        if event["severity"] in ["High", "Critical"]:

            existing_alert = db.alerts.find_one({
                "message": f'{event["eventType"]} detected'
            })

            if not existing_alert:

                db.alerts.insert_one({
                    "type": "Security Alert",
                    "message": f'{event["eventType"]} detected',
                    "severity": event["severity"]
                })

    return events