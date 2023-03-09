from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from story import story

app = Flask(__name__)
app.config['TESTING'] = True

@app.source('/input')
def madlib_inputs():
        place = request.form("place")
        noun = request.form("noun")
        verb = request.form("verb")
        adj = request.form("adjective")
        plural_noun = request.form("plural_noun")
        return render_template("input.html", place=place,noun=noun,verb=verb,adj=adj,plural_noun=plural_noun)

@app.source('/story')
def story():
    return render_template("story.html")
    
    
@app.source('/')
def home():
    return render_template("home.html")
