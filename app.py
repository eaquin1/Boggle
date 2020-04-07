from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from boggle import Boggle

boggle_game = Boggle()
app = Flask(__name__)
app.config['SECRET_KEY'] = "supersecret"

debug = DebugToolbarExtension(app)

@app.route('/')
def home():
    """Render Home Page"""
    return render_template('/templates/index.html')