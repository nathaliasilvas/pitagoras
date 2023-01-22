from flask import Flask, jsonify, request
import math

app = Flask(__name__)


@app.route("/calculator", methods=["GET"])
def set_name():
    a = request.args.to_dict().get("a")
    b = request.args.to_dict().get("b")

    if a is None or b is None:
        return jsonify({"message": "Do you must provide params 'a' and 'b'"})

    return jsonify({"result": math.sqrt((float(a) ** 2) + (float(b) ** 2))})


if __name__ == "__main__":
    app.run(debug=True)