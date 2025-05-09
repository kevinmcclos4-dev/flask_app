from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        'message': 'Welcome to the Flask API',
        'status': 'success'
    })

@app.route('/health')
def health():
    return jsonify({
        'status': 'healthy',
        'version': '1.0.0'
    })

@app.route('/api-data')
def api_data():
    return jsonify({
        'data': [
            {'id': 1, 'name': 'Item 1'},
            {'id': 2, 'name': 'Item 2'},
            {'id': 3, 'name': 'Item 3'},
            {'id': 4, 'name': 'Item 4'},
            {'id': 5, 'name': 'Item 5'},
            {'id': 6, 'name': 'Item 6'}
        ]
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) 