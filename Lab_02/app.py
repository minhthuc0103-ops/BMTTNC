from flask import Flask, render_template, request
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher
from cipher.playfair import PlayFairCipher
from cipher.transposition import TranspositionCipher

app = Flask(__name__)

caesar_cipher = CaesarCipher()
vigenere_cipher = VigenereCipher()
railfence_cipher = RailFenceCipher()
playfair_cipher = PlayFairCipher()
transposition_cipher = TranspositionCipher()

# ==================== HOME ====================
@app.route("/")
def home():
    return render_template('index.html')

# ==================== CAESAR ====================
@app.route("/caesar")
def caesar():
    return render_template('caesar.html')

@app.route("/caesar/encrypt", methods=['POST'])
def caesar_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKey'])
    result = caesar_cipher.encrypt_text(text, key)
    return render_template('caesar.html', encrypt_result=result, plain_text=text, key=key)

@app.route("/caesar/decrypt", methods=['POST'])
def caesar_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKey'])
    result = caesar_cipher.decrypt_text(text, key)
    return render_template('caesar.html', decrypt_result=result, cipher_text=text, key=key)

# ==================== VIGENERE ====================
@app.route("/vigenere")
def vigenere():
    return render_template('vigenere.html')

@app.route("/vigenere/encrypt", methods=['POST'])
def vigenere_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKey']
    result = vigenere_cipher.vigenere_encrypt(text, key)
    return render_template('vigenere.html', encrypt_result=result, plain_text=text, key=key)

@app.route("/vigenere/decrypt", methods=['POST'])
def vigenere_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKey']
    result = vigenere_cipher.vigenere_decrypt(text, key)
    return render_template('vigenere.html', decrypt_result=result, cipher_text=text, key=key)

# ==================== RAIL FENCE ====================
@app.route("/railfence")
def railfence():
    return render_template('railfence.html')

@app.route("/railfence/encrypt", methods=['POST'])
def railfence_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKey'])
    result = railfence_cipher.rail_fence_encrypt(text, key)
    return render_template('railfence.html', encrypt_result=result, plain_text=text, key=key)

@app.route("/railfence/decrypt", methods=['POST'])
def railfence_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKey'])
    result = railfence_cipher.rail_fence_decrypt(text, key)
    return render_template('railfence.html', decrypt_result=result, cipher_text=text, key=key)

# ==================== PLAYFAIR ====================
@app.route("/playfair")
def playfair():
    return render_template('playfair.html')

@app.route("/playfair/encrypt", methods=['POST'])
def playfair_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKey']
    matrix = playfair_cipher.create_playfair_matrix(key)
    result = playfair_cipher.playfair_encrypt(text, matrix)
    return render_template('playfair.html', encrypt_result=result, plain_text=text, key=key)

@app.route("/playfair/decrypt", methods=['POST'])
def playfair_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKey']
    matrix = playfair_cipher.create_playfair_matrix(key)
    result = playfair_cipher.playfair_decrypt(text, matrix)
    return render_template('playfair.html', decrypt_result=result, cipher_text=text, key=key)

# ==================== TRANSPOSITION ====================
@app.route("/transposition")
def transposition():
    return render_template('transposition.html')

@app.route("/transposition/encrypt", methods=['POST'])
def transposition_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKey'])
    result = transposition_cipher.encrypt(text, key)
    return render_template('transposition.html', encrypt_result=result, plain_text=text, key=key)

@app.route("/transposition/decrypt", methods=['POST'])
def transposition_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKey'])
    result = transposition_cipher.decrypt(text, key)
    return render_template('transposition.html', decrypt_result=result, cipher_text=text, key=key)

# ==================== MAIN ====================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)