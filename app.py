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

@app.route('/score', methods=["POST"])
def save_score():
    """Save the score"""
    score = request.json["score"]
    high_score = session.get("high_score", 0)
    nplays = session.get("nplays", 0)

    session['nplays'] = nplays + 1
    session['high_score'] = max(high_score, score)
    
    return jsonify(brokeRecord=score > high_score)

