from flask import Flask, render_template, request
import calendar

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>Lauke salta!</h1>"


@app.route("/kazkas/<word>")
def user(word):
    return f"{word} {word} {word} {word} {word}"


@app.route("/keliamieji")
def keliamieji():
    metai_keliami = [metai for metai in range(1900, 2100) if calendar.isleap(metai)]
    return render_template("uzduotis.html", sarasas=metai_keliami)


@app.route("/ar_keliamieji", methods=["GET", "POST"])
def k_metai():
    metai_keliami = [metai for metai in range(1900, 2100) if calendar.isleap(metai)]
    if request.method == "POST":
        metai = int(request.form["metai"])
        if metai in metai_keliami:
            ar_keliami = "Taip metai yra keliamieji!"
        else:
            ar_keliami = "Ne, metai nera keliamieji!"
        return render_template("uzduotis2.html", ar_metai=ar_keliami)
    else:
        return render_template("uzduotis.html")


if __name__ == "__main__":
    app.run(debug=True)
