from flask import Flask, request, send_file, send_from_directory, jsonify
from flask_cors import CORS
import requests
from io import BytesIO

app = Flask(__name__, static_folder='.')
CORS(app)  # Allow requests from any origin

# Serve the HTML file
@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

# Image search route
@app.route('/search')
def search():
    query = request.args.get('q', '')
    if not query:
        return jsonify({'error': 'Query is required'}), 400

    url = f"https://source.unsplash.com/800x600/?{query}"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            img = BytesIO(response.content)
            return send_file(img, mimetype='image/jpeg')
        else:
            return jsonify({'error': 'Image not found'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
