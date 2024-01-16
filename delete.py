from main_db import app, db, Message


with app.app_context():
    jonas = Message.query.get(1)
    db.session.delete(jonas)
    db.session.commit()
    print(Message.query.all())
