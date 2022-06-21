from flask import Flask, render_template, request
from stories import story

app = Flask(__name__)

@app.route('/')
def index():
    """Show input form"""

    prompts = story.prompts

    return render_template('home.html', prompts=prompts)

@app.route('/story')
def show_story():
    """Return story with user input"""

    text = story.generate(request.args)

    return render_template('story.html', text=text)