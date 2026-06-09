from pymongo import MongoClient
from dotenv import load_dotenv
import os

print("Loading mongodb.py...")

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")

client = MongoClient(MONGO_URI)

try:
    client.admin.command("ping")
    print("MongoDB Connected Successfully!")
except Exception as e:
    print("MongoDB Connection Failed:", e)

db = client["cloud_monitor"]