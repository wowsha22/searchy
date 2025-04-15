from flask import Flask, request, jsonify, send_from_directory
import requests

app = Flask(__name__, static_url_path='', static_folder='.')

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/search')
def search():
    query = request.args.get('q', '')
    url = f'https://duckduckgo.com/i.js'
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }
    params = {
        'q': query
    }

    try:
        response = requests.get(url, headers=headers, params=params, timeout=5)
        data = response.json()
        images = [img['image'] for img in data.get('results', [])]
        return jsonify({'images': images})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
