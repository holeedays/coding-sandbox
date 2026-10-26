from flask import Flask, redirect, render_template, request, url_for
import models

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # check whether the submission is for the expenses or revenues field
        if ("expenses__entry_date" in request.form):
            models.add_expense(
                request.form["expenses__entry_date"],
                request.form["expenses__description"],
                request.form["expenses__category"],
                float(request.form["expenses__amount"])
            )
        else:
            models.add_revenue(
                request.form["revenues__entry_date"],
                request.form["revenues__description"],
                request.form["revenues__category"],
                float(request.form["revenues__amount"])
            )
            
        # return redirect(url_for("index"))
    return render_template("index.html", expenses=models.get_expenses(), revenues=models.get_revenues())


if (__name__ == "__main__"):
    app.run(port=3000, debug=True)
