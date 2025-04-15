from flask import Flask, request, jsonify, send_file
import requests
from io import BytesIO

app = Flask(__name__, static_url_path='', static_folder='.')

# Serve the index.html for the web app
@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

# API route for image search
@app.route('/search')
def search():
    query = request.args.get('q', '')
    if not query:
        return jsonify({'error': 'Query parameter is required'}), 400
    
    # Unsplash search URL for random images based on the query
    url = f"https://source.unsplash.com/800x600/?{query}"
    
    try:
        # Fetch the image from Unsplash (the image is returned as bytes)
        response = requests.get(url)
        
        if response.status_code == 200:
            # Send the image back to the client
            img = BytesIO(response.content)
            return send_file(img, mimetype='image/jpeg')  # Adjust mime type if necessary
        else:
            return jsonify({'error': 'Failed to retrieve image from Unsplash'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Make sure the Flask app runs on the correct host and port
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
