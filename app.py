from flask import Flask, request
from pymongo import MongoClient
import os

app = Flask(__name__)

# Mongo URI নেওয়া হবে environment থেকে
MONGO_URI = os.environ.get("MONGO_URI", "mongodb://localhost:27017/")
client = MongoClient(MONGO_URI)
db = client['filebot']
collection = db['files']

@app.route('/')
def home():
    return "Filebot is running with Gunicorn!"

if __name__ == '__main__':
    # Local run এর জন্য
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
