from flask import Flask
from flask import request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///passmanager.sqlite3'
 
app.config['SQLALCEMY_TRACK_MODIFICATIONS']  = False
 
db = SQLAlchemy(app)
ma = Marshmallow(app)
 

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)