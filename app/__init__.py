from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, current_user
from flask_wtf import CSRFProtect

app = Flask('app')
app.config.from_pyfile('config.py')
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.init_app(app)
csrf = CSRFProtect(app)

from app import views, commands