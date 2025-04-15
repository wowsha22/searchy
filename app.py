from flask import Flask, request, send_file, send_from_directory, jsonify
import requests
from io import BytesIO
import os

app = Flask(__name__, static_folder='.')

# Serve index.html at root
@app.route('/')
def index():
    return send_from_directory('.', 'index.html')  # Ensure 'index.html' is in the same folder as app.py

# API route for image search
@app.route('/search')
def search():
    query = request.args.get('q', '')
    if not query:
        return jsonify({'error': 'Query parameter is required'}), 400

    url = f"https://source.unsplash.com/800x600/?{query}"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            img = BytesIO(response.content)
            return send_file(img, mimetype='image/jpeg')
        else:
            return jsonify({'error': 'Failed to retrieve image from Unsplash'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
