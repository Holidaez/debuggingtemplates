import os
from flask import Flask, render_template, request, session, redirect
from flask_migrate import Migrate
from flask_login import LoginManager
from .models import db, User
from .seeds import seed_commands
from .config import Config
from .routes import business_routes, review_routes
app = Flask(__name__)
login = LoginManager(app)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

app.cli.add_command(seed_commands)

app.config.from_object(Config)
app.register_blueprint(business_routes.business_routes, url_prefix='/api/business')
# app.register_blueprint(review_routes, url_prefix='/api/review')
db.init_app(app)
Migrate(app, db)
