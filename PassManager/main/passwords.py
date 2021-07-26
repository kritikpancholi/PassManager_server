import PassManager
from flask import Flask, request, jsonify, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask import request, jsonify
from PassManager.models import User, Password
from PassManager import db , ma

password_blueprint = Blueprint('password_blueprint', __name__)

class PasswordSchema(ma.Schema):
    class Meta:
        fields = ("email", "title", "user_password" , "user_id" ,"id")



password_schema = PasswordSchema()
passwords_schema = PasswordSchema(many=True)

@password_blueprint.route('/', methods=['GET'])
def home():
    return "<h1>Kritik</h1>"

@password_blueprint.route('/get_password', methods=['GET'])
def showPassword():
    id = request.args.get('user_id')
    val = Password.query.filter_by(user_id=id).all()
    if val:
        return jsonify(passwords_schema.dump(val))
    return jsonify({'status_code': 404}) 

@password_blueprint.route('/create_password', methods=['POST' , 'GET'])
def createPassword():      
    id= request.json.get('user_id')
    email_id= request.json.get('email')
    password= request.json.get('user_password')
    pass_title= request.json.get('title')
    new_entry_password= Password(email=email_id, user_id=id, user_password=password, title=pass_title)
    db.session.add(new_entry_password)
    db.session.commit()
    val= Password.query.filter_by(user_id = id).all()

    #print(jsonify(data = val))

    return jsonify(passwords_schema.dump(val))

@password_blueprint.route('/show_all_passwords', methods=['GET'])
def show_all():
    val = Password.query.all()
    return jsonify(passwords_schema.dump(val))

@password_blueprint.route('/delete_password',methods = ['DELETE'])
def delete_password():
    to_delete_id = request.json.get('id')
    val = Password.query.filter_by(id = to_delete_id).first()
    db.session.delete(val)
    db.session.commit()

    return "<h1>delete</h1>"
