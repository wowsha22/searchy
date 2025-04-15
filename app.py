from flask import Flask, request, send_file, jsonify
from flask_cors import CORS
import requests
from io import BytesIO

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
        # Use a more reliable Unsplash endpoint for random image based on query
        url = f"https://source.unsplash.com/random/800x600/?{query},photo"
        print("📡 Requesting image from:", url)

        response = requests.get(url, timeout=5)
        print("📦 Response status code:", response.status_code)

        if response.status_code == 200:
            return send_file(BytesIO(response.content), mimetype='image/jpeg')
        else:
            print("🚫 Failed to get image from Unsplash")
            return jsonify({'error': 'Image not found'}), 500

    except Exception as e:
        print("💥 Server error:", e)
        return jsonify({'error': str(e)}), 500
