from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask import request, jsonify

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///passmanager.sqlite3'
app.config['SQLALCEMY_TRACK_MODIFICATIONS']= False

db = SQLAlchemy(app)

from PassManager.main.routes import main
app.register_blueprint(main)
