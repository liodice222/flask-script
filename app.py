      #!/bin/bash
      # Update and install required packages
      dnf update -y
      dnf install -y python3 python3-pip git

      # Install Flask
      pip3 install flask gunicorn

      # Create a sample Flask app
      mkdir -p /opt/flask-app
      cat > /opt/flask-app/app.py <<'EOL'
      from flask import Flask, jsonify
      import random
      import time

      app = Flask(__name__)

      @app.route('/')
      def hello():
          return jsonify({"message": "Hello from Flask on OCI!"})

      @app.route('/metrics')
      def metrics():
          # Generate some random metrics for Grafana to visualize
          cpu = random.uniform(0, 100)
          memory = random.uniform(0, 100)
          return jsonify({
              "cpu_usage": cpu,
              "memory_usage": memory,
              "timestamp": time.time()
          })

      if __name__ == '__main__':
          app.run(host='0.0.0.0', port=5000)
      EOL
