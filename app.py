from flask import Flask, render_template, request

# Custom modules
import MorseFunctions
import RSA

app = Flask(__name__)


# ? Home Page
@app.route('/')
def home():

    return render_template('home.html')

# ? Kids Games


# Simon Game
@app.route('/simon')
def simon():

    return render_template('simon.html')


# Card Game
@app.route('/cardgame')
def cardgame():

    return render_template('cardgame.html')


# Math Game
@app.route('/mathgame')
def mathgame():

    return render_template('mathgame.html')


# ? Encryption Page
@app.route('/encryption')
def encryption():

    return render_template('encryption.html')


# Morse Code
@app.route('/encryption/morse', methods=['GET', 'POST'])
def morse():

    if request.method == 'POST':

        morse_to_eng_text = request.form.get('morse_to_eng', None)
        eng_to_morse_text = request.form.get('eng_to_morse', None)
        result = {}

        if morse_to_eng_text:
            result["original"] = morse_to_eng_text
            result['morse_to_eng'] = MorseFunctions.morse_to_eng(
                morse_to_eng_text)
        if eng_to_morse_text:
            result["original"] = eng_to_morse_text
            result['eng_to_morse'] = MorseFunctions.eng_to_morse(
                eng_to_morse_text)

        return render_template('morse.html', result=result)

    return render_template('morse.html', result=None)


# RSA
@app.route('/encryption/rsa', methods=['GET', 'POST'])
def rsa():

    if request.method == 'POST':
        originaltext = request.form.get('originaltext', None)

        result = {}
        result["originaltext"] = originaltext

        ciphertext, plaintext, public_key, private_key = RSA.getEncryptedAndDecryptedMessage(
            originaltext)

        result["ciphertext"] = ciphertext
        result["deciphertext"] = plaintext
        result["public_key"] = public_key
        result["private_key"] = private_key

        return render_template('rsa.html', result=result)

    return render_template('rsa.html')


if __name__ == "__main__":
    app.run(debug=True)
