from flask import Flask, render_template, request
from pathlib import Path

import pandas as pd
from .dogs import get_dogs, get_dogs_local


app: Flask = Flask(__name__)

# to run flask
# run either in this dir: flask run (this only works if the app file is named app.py or wsgi.py)
# if other dir: flask --app [app_path] run (don't include the .py here)

CSV_FILE_PATH: Path = Path(__file__).parent / "data" / "votes.csv"

# index decorator
@app.route("/")
def index_view() -> str:
    return render_template("index.html", dogs=get_dogs())

# dealing with POST and GET requests here
@app.route("/test-form", methods=["GET", "POST"])
def test_form() -> str:
    message: str = ""
    winner: str = ""
    if request.method == "POST":
        dog_a = request.form["dog_a"]
        dog_b = request.form["dog_b"]
        winner = request.form["winner"]
        print("Dog A:", dog_a)
        print("Dog B:", dog_b)
        print("Winner:", winner)
        message = "Vote received! Here are two more dogs."

        # now convert it to a CSV file here using pandas
        vote = pd.DataFrame([{
            "dog_a": request.form["dog_a"],
            "dog_b": request.form["dog_b"],
            "winner": request.form["winner"],
        }])

        if CSV_FILE_PATH.exists():
            previous_votes = pd.read_csv(CSV_FILE_PATH)
            # concat initial dataframe with new one
            vote = pd.concat([previous_votes, vote], ignore_index=True)

        vote.to_csv(CSV_FILE_PATH, index=False)

    return render_template("test_form.html", dogs=get_dogs(), message=message, winner=winner)


################################################################## ALT METHODS

# index decorator
@app.route("/alt")
def alt_index_view() -> str:
    return render_template("index_alt.html", dogs=get_dogs_local())

# dealing with POST and GET requests here
@app.route("/alt/test-form", methods=["GET", "POST"])
def alt_test_form() -> str:
    message: str = ""
    if request.method == "POST":
        dog_a = request.form["dog_a"]
        dog_b = request.form["dog_b"]
        winner = request.form["winner"]
        print("Dog A:", dog_a)
        print("Dog B:", dog_b)
        print("Winner:", winner)
        message = "Vote received! Here are two more dogs."
    return render_template("test_form_alt.html", dogs=get_dogs_local(), message=message)

# you can also run it via a module
# just do python -m [app_name] (you know the drill)
if (__name__ == "__main__"):
    app.run(debug=True)