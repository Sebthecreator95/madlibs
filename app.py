  from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)


@app.route("/pickastory")
def pick_story():
    """Generate and show form to ask words."""
    return render_template("pickAStory.html",
                           stories=stories.values())

@app.route("/questions")
def ask_questions():
    """Generate and show form to ask words."""

    story_name = request.args["story_class_name"]
    story = stories["story_class_name"]

    prompts = story.prompts

    return render_template("madlibForm.html",
                           story_class_name=story_class_name,
                           title=story.title,
                           prompts=prompts)

@app.route("/story")
def show_story():
    """Show story result."""
    story_class_name = request.args["story_class_name"]
    story = stories["story_class_name"]

    text = story.generate(request.args)

    return render_template("story.html",
                           title=story.title,
                           text=text)

