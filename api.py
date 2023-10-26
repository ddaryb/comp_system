from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/calculator', methods=['POST'])
def calculate():
    data = request.get_json()

    if 'operation' not in data or 'value1' not in data or 'value2' not in data:
        return jsonify({"error": "Invalid Request"}), 400

    operation = data['operation']
    value1 = data['value1']
    value2 = data['value2']

    if operation == 'add':
        result = value1 + value2
    elif operation == 'subtract':
        result = value1 - value2
    elif operation == 'multiply':
        result = value1 * value2
    elif operation == 'divide':
        if value2 != 0:
            result = value1 / value2
        else:
            return jsonify({"error": "Division by zero"}), 400
    else:
        return jsonify({"error": "Unsupported operation"}), 400

    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)
