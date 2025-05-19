from flask import Flask, request
from pymongo import MongoClient
import os

app = Flask(__name__)

# MongoDB URI from environment variable
MONGO_URI = os.environ.get("MONGO_URI", "mongodb://localhost:27017/")
client = MongoClient(MONGO_URI)
db = client['filebot']
collection = db['files']

@app.route('/')
def home():
    return "Filebot is running!"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Render এর জন্য দরকারি
    app.run(host='0.0.0.0', port=port)
