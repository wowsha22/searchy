from flask import Flask, request, jsonify, send_from_directory
import requests

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
    
    # Make the request to Unsplash
    try:
        response = requests.get(url)
        
        # If the response is successful, return the image URL
        if response.status_code == 200:
            image_url = response.url
            return jsonify({'image': image_url})
        else:
            return jsonify({'error': 'Failed to retrieve image from Unsplash'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Make sure the Flask app runs on the correct host and port
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
