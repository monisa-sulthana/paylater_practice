from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/", methods=["GET"])
def homepage():
    return render_template("index.html")

@app.route("/about", methods=["GET"])
def about():
    return render_template("about.html")

@app.route("/merchants", methods=["GET", "POST"])
def merchants():
    if request.form == "POST":
        mer_id = request.form["mer_id"]
        app = request.form["app"]
        txt_rate = request.form["txt_rate"]
    return render_template("merchants.html")

@app.route("/users", methods=["GET", "POST"])
def users():
    if request.form == "POST":
        user_id = request.form["user-id"]
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        address = request.form["address"]
        credit_limit = request.form["credit_limit"]
        due = request.form["due"]
    return render_template("users.html")

@app.route("/reports", methods=["GET"])
def reports():
    return render_template("reports.html")

app.run(debug=True)