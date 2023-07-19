from flask import Flask, request, jsonify

app = Flask(__name__)

def encode_to_binary(message):
    binary_code = ""
    for char in message:
        binary_code += bin(ord(char))[2:].zfill(8)
    return binary_code

def decode_binary(binary_code):
    decoded_message = ""
    for i in range(0, len(binary_code), 8):
        binary_char = binary_code[i:i+8]
        decoded_message += chr(int(binary_char, 2))
    return decoded_message

@app.route('/encode', methods=['POST'])
def encode():
    data = request.get_json()
    message = data['message']
    encoded = encode_to_binary(message)
    return jsonify({'encoded': encoded})

@app.route('/decode', methods=['POST'])
def decode():
    data = request.get_json()
    binary_code = data['binary_code']
    decoded = decode_binary(binary_code)
    return jsonify({'decoded': decoded})

@app.route('/menu', methods=['POST'])
def menu():
    data = request.get_json()
    choice = data['choice']

    if choice == "1":
        message = data['message']
        encoded = encode_to_binary(message)
        return jsonify({'encoded': encoded})
    elif choice == "2":
        binary_code = data['binary_code']
        decoded = decode_binary(binary_code)
        return jsonify({'decoded': decoded})
    elif choice == "3":
        return jsonify({'message': 'Exiting the program...'})
    else:
        return jsonify({'message': 'Invalid choice. Please try again.'})

if __name__ == '__main__':
    app.run()
