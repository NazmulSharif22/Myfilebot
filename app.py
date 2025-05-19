from flask import Flask, request, jsonify
import cloudinary
import cloudinary.uploader
import os

app = Flask(__name__)

# Cloudinary config
cloudinary.config(
  cloud_name=os.getenv('CLOUD_NAME'),
  api_key=os.getenv('API_KEY'),
  api_secret=os.getenv('API_SECRET')
)

@app.route('/')
def index():
    return "Filebot with permanent cloud link is live!"

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    try:
        upload_result = cloudinary.uploader.upload_large(
            file,
            resource_type="auto"  # supports video, image, etc
        )
        return jsonify({'link': upload_result['secure_url']}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
