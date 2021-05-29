from enum import unique
from types import MethodType
from flask import Flask
from flask import request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import passwords

app = Flask(__name__)
 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///passmanager.sqlite3'
 
app.config['SQLALCEMY_TRACK_MODIFICATIONS']  = False
 
db = SQLAlchemy(app)
ma = Marshmallow(app)
 
class users (db.Model):
    id = db.Column(db.Integer , primary_key = True)
    email = db.Column(db.String(100) , unique = True)
    password  = db.Column(db.String )
 
    def __init__(self , email ,password) :
        self.email  = email
        self.password = password
   
class userSchema(ma.Schema):
    class Meta:
        fields = ('id','email','password')

userschema = userSchema()
user1schema = userSchema(many=True)

@app.route('/login' ,methods = ['POST' , 'GET'] )
def login():
    user_email = request.args.get('email')
    
    user_password  = request.args.get('password')
    val = users.query.filter_by(email=user_email , password = user_password ).first()
    if val :
        return userSchema().jsonify(val)
    
    new_email = users(email = user_email,password = user_password)
    db.session.add(new_email)
    db.session.commit()
    
    return  userSchema().jsonify(new_email)


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)