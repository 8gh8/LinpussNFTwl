from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/check', methods=['POST'])
def check_address():
    data = request.json
    address = data.get("address", "").lower()
    white_list = ["0x123456789abcdef", "0xabcdef123456789"]  # Ваші дані
    if address in white_list:
        return jsonify({"message": "Congratulations, you are in the White List!"})
    return jsonify({"message": "Sorry, you are not in the White List."})

if __name__ == '__main__':
    app.run(debug=True)
