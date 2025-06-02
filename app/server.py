from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello from Self-Healing App!"

@app.route('/healthz')
def healthz():
    return "OK", 200

@app.route('/ready')
def ready():
    return "Ready", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
