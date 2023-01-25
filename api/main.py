from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import math

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/calculator', methods=['GET'])
@cross_origin()
def calculator():
    a = request.args.to_dict().get('a')
    b = request.args.to_dict().get('b')

    if a is None or b is None:
        return jsonify({'message': 'Do you must provide params \'a\' and \'b\''})

    return jsonify({'result': math.sqrt((float(a) ** 2) + (float(b) ** 2))})


if __name__ == '__main__':
    app.run(debug=True)
