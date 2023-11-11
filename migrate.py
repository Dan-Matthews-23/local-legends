from local_legends import app, db, app_context

with app.app_context().push():
    db.create_all()
