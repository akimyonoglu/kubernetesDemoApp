import os

from flask import Flask
from flask import jsonify
app = Flask(__name__)
app.debug = True

@app.route('/')
def hello_world():
    return jsonify(os.environ)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8082)
