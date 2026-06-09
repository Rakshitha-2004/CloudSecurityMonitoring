from database.mongodb import db
from services.s3_service import get_buckets
from services.iam_service import get_users

def get_dashboard_summary():

    total_buckets = len(get_buckets())
    total_iam_users = len(get_users())

    active_security_events = db.security_events.count_documents({})

    critical_alerts = db.alcerts.count_documents({
        "severity": "Critical"
    })

    return {
        "totalBuckets": total_buckets,
        "totalIAMUsers": total_iam_users,
        "activeSecurityEvents": active_security_events,
        "criticalAlerts": critical_alerts
    }