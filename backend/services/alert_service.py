from services.s3_service import get_buckets
from database.mongodb import db

def generate_alerts():

    buckets = get_buckets()

    for bucket in buckets:

        alert = {
            "type": "S3 Bucket Detected",
            "severity": "Low",
            "bucket": bucket["bucket_name"]
        }

        db.alerts.insert_one(alert)
        return {"message": "Alerts generated successfully"}
