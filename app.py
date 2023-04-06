from flask import Flask, render_template, request

# Custom modules
import MorseFunctions

app = Flask(__name__)


# ? Home Page
@app.route('/')
def home():

    return render_template('home.html')

# ? Kids Games


@app.route('/simon')
def simon():

    return render_template('simon.html')


# ? Encryption Page
@app.route('/encryption')
def encryption():

    return render_template('encryption.html')


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


if __name__ == "__main__":
    app.run(debug=True)
