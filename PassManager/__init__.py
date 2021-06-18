from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask import request, jsonify
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///passmanager.sqlite3'
app.config['SQLALCEMY_TRACK_MODIFICATIONS']= False

db = SQLAlchemy(app)
ma = Marshmallow(app)

from PassManager.main.passwords import password_blueprint
app.register_blueprint(password_blueprint)

from PassManager.main.user_auth_route import user_auth
app.register_blueprint(user_auth)