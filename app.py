from flask import Flask, request, render_template, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from boggle import Boggle

boggle_game = Boggle()
app = Flask(__name__)
app.config['SECRET_KEY'] = "supersecret"

debug = DebugToolbarExtension(app)

@app.route('/')
def home():
    """Render Home Page"""
    board = boggle_game.make_board()
    session['board'] = board
    return render_template('index.html', board=board)

@app.route('/check-word')
def check_word():
    """Check if the word in the dictionary"""
    word = request.args["word"]
    board = session['board']
    validity = boggle_game.check_valid_word(board, word)

    return jsonify({'result': validity})
