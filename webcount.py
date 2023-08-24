from flask import Flask, request, jsonify

app = Flask(__name__)
counter = 0

@app.route('/', methods=['GET', 'POST'])
def counter_service():
    global counter

    if request.method == 'POST':
        counter += 1
        return jsonify({'message': 'POST request received'}), 201

    if request.method == 'GET':
        return jsonify({'counter': counter}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
