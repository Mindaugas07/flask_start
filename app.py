from main_db import db, Message, app
from flask import request, render_template, redirect


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]
        query = Message(name, email, message)
        db.session.add(query)
        db.session.commit()
        return render_template("greetings.html", vardas=name)
    elif request.method == "GET":
        return render_template("login.html")


@app.route(
    "/all_data",
)
def all_datas():
    all_rows = Message.query.all()
    return render_template("all_data.html", sarasas=all_rows)


@app.route("/delete", methods=["POST", "GET"])
def delete():
    if request.method == "GET":
        all_rows = Message.query.all()
    else:
        email = request.form["email"]
        message = Message.query.filter_by(email=email).first()
        print(message)
        if message:
            db.session.delete(message)
            db.session.commit()
            all_rows = Message.query.all()
    return render_template("delete.html", sarasas=all_rows)


if __name__ == "__main__":
    app.run(debug=True)
