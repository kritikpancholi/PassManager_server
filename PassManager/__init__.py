from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask import request, jsonify
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///passmanager.sqlite3'
app.config['SQLALCEMY_TRACK_MODIFICATIONS']= False

db = SQLAlchemy(app)
ma = Marshmallow(app)

from PassManager.main.routes import main
app.register_blueprint(main)
