from flask import Flask, render_template, jsonify
from mnemonic import Mnemonic

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate')
def generate_mnemonic():
    mnemo = Mnemonic("english")
    words = mnemo.generate(strength=128)
    return jsonify(words=words)

if __name__ == '__main__':
    app.run(debug=True)
