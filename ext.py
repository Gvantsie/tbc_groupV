from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
app.config["SECRET_KEY"] = "kcajsciah238e298e742/*^"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydb.db"


db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"