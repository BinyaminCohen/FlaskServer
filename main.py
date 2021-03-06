from flask import Flask, jsonify
from multiprocessing import Value

counter = Value('i', 0)
app = Flask(__name__)


@app.route('/count')
def index():
    with counter.get_lock():
        counter.value += 1
        out = counter.value

    return jsonify(count=out)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
