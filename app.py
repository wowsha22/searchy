from flask import Flask, request, send_file, jsonify
from flask_cors import CORS
import requests
from io import BytesIO
import os

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return send_file('index.html')

@app.route('/search')
def search():
    query = request.args.get('q', '').strip()
    print("🔍 Received query:", query)

    if not query:
        return jsonify({'error': 'No query provided'}), 400

    try:
        # Use Unsplash random endpoint without specifying exact resolution
        url = f"https://source.unsplash.com/random/?{query},photo"
        print("📡 Requesting image from:", url)

        response = requests.get(url, timeout=5)
        print("📦 Response status code:", response.status_code)

        # Check if the response is valid, otherwise fallback to a default image
        if response.status_code == 200:
            return send_file(BytesIO(response.content), mimetype='image/jpeg')
        else:
            print("🚫 Failed to get image from Unsplash")
            # Fallback to a locally stored default image if the search fails
            default_image_path = os.path.join(app.root_path, 'static', 'default_image.jpg')
            return send_file(default_image_path, mimetype='image/jpeg')

    except Exception as e:
        print("💥 Server error:", e)
        return jsonify({'error': str(e)}), 500
