from flask import Flask
from database.mongodb import db
from services.s3_service import get_buckets
from services.iam_service import get_users 
from services.security_service import get_security_events 
from services.simulate_attack_service import simulate_attack 
from services.dashboard_service import get_dashboard_summary

app = Flask(__name__)

@app.route("/")
def home():
    return {"message": "Backend Running"}

@app.route("/test-db")
def test_db():
    db.alerts.insert_one({
        "type": "Test Alert",
        "severity": "Low"
    })
    return {"message": "Data inserted successfully"}

@app.route("/api/buckets")
def list_buckets():
    return get_buckets()

@app.route("/api/alerts")
def get_alerts():
    alerts = list(db.alerts.find({}, {"_id": 0}))
    return alerts

@app.route("/api/iam-users")
def iam_users():
    return get_users() 

@app.route("/api/security-events")
def security_events():
    return get_security_events() 

@app.route("/api/simulate-attack")
def simulate_attack_route():
    return simulate_attack() 

@app.route("/api/dashboard-summary")
def dashboard_summary():
    return get_dashboard_summary()

if __name__ == "__main__":
    app.run(debug=True)