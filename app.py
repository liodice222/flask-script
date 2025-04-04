from flask import Flask, jsonify, request

import random
import time

# Initialize the Flask application
app = Flask(__name__)

# Define a simple route for the homepage
@app.route('/')
def index():
    return "Welcome to the Flask App!"

@app.route('/metrics')
def metrics():
    #generate random metrics
    cpu = random.uniform(0,100)
    memory = random.uniform(0,100)
    return jsonify ({
        "cpu_usage": cpu,
        "memory_usage": memory
    })
# Define a route that returns JSON data
@app.route('/api/data', methods=['GET'])
def get_data():
    sample_data = {
        'message': "Hello from Flask!",
        'version': '1.0'
    }
    return jsonify(sample_data)

# Define a route to accept POST data
@app.route('/api/echo', methods=['POST'])
def echo():
    data = request.get_json()
    if data is None:
        return jsonify({'error': 'No JSON payload provided.'}), 400
    return jsonify({'you_sent': data})

# Run the application if executed directly
if __name__ == '__main__':
    # Setting debug=True for development allows automatic reloads on code changes.
    app.run(host='0.0.0.0', port=5000, debug=True)
