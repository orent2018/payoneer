from flask import Flask, request, jsonify

app = Flask(__name__)

# Define the file to store the counter value
counter_file = "web_counter.txt"

# Initialize the counter
try:
    with open(counter_file, "r") as f:
        counter = int(f.read())
except FileNotFoundError:
    counter = 0

@app.route("/", methods=["GET", "POST"])
def counter_service():
    global counter

    if request.method == "POST":
        # Increment the counter on a POST request
        counter += 1
        with open(counter_file, "w") as f:
            f.write(str(counter))

        return jsonify({'message': 'POST request received'}), 201 

    else:
      # Return the current counter value on every GET request
      return jsonify({'counter': counter}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)

