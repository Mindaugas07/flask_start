from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def user():
    return render_template("index.html")


@app.route("/calculations")
def calculations():
    return render_template("calculations.html")


@app.route("/say_hello/<name>")
def name(name):
    return {"name": name}


# @app.route("/say_hello/<name>")
# def user(name):
#     return f"Labas, {name}"


@app.route("/names")
def home():
    vardai = ["Jonas", "Antanas", "Petras"]
    return render_template("names.html", sarasas=vardai)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        vardas = request.form["vardas"]
        return render_template("greetings.html", vardas=vardas)
    else:
        return render_template("login.html")


if __name__ == "__main__":
    app.run()
