from flask import Flask, render_template, request

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

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/encode", methods=["POST"])
def encode():
    message = request.form.get("message")
    encoded = encode_to_binary(message)
    return render_template("result.html", binary_code=encoded)

@app.route("/decode", methods=["POST"])
def decode():
    binary_code = request.form.get("binary_code")
    decoded = decode_binary(binary_code)
    return render_template("result.html", decoded_message=decoded)

if __name__ == "__main__":
    app.run()
    
