import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

if os.path.exists("env.py"):
    import env  # noqa


if os.path.exists("env.py"):
    import env  # noqa
app = Flask(__name__)
# Database configuration
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
if os.environ.get("DEVELOPMENT") == "True":
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")  # local
else:
    uri = os.environ.get("DATABASE_URL")
    if uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)
    app.config["SQLALCHEMY_DATABASE_URI"] = uri  # heroku
# Additional database configuration options
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# Initialize Flask extensions
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from local_legends import routes  #noqa 