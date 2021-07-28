import PassManager
from flask import Flask, request, jsonify, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask import request, jsonify
from PassManager.models import User, Password
from PassManager import db , ma

user_auth = Blueprint('user_auth', __name__)

class UserSchema(ma.Schema):
    class Meta:
        fields = ("id" , "email" , "password")

user_schema = UserSchema()
users_schema = UserSchema(many=True)

@user_auth.route('/signIn' , methods =['POST'])
def signIn():
    user_email = request.json.get('email')
    user_password = request.json.get('password')

    val = User.query.filter_by(email = user_email , password = user_password).first()
    if(val):
        return 'already a user' , 400
    user = User(email= user_email , password=user_password)

    db.session.add(user)
    db.session.commit()
    
    val = User.query.filter_by(email = user_email , password = user_password).first()
    return jsonify(
        id = val.id,
    )



@user_auth.route('/login', methods=['GET'])
def login():
    user_email = request.args.get('email')
    user_password = request.args.get('password')
    val = User.query.filter_by(email = user_email ,password=user_password).first()
    if(val):
        return jsonify(
            id = val.id ,
        ) 
    return 'email is not register!',400 


@user_auth.route('/show_all', methods=['GET'])
def all():
  
    val = User.query.all()

    return jsonify(users_schema.dump(val))
    
