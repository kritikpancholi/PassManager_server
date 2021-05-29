from flask import Flask, request, jsonify, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask import request, jsonify
from PassManager.models import User, Password

main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
def home():
    return "<h1>Kritik is gay</h1>"

@main.route('/get_password', methods=['GET'])
def showPassword():
    id = request.args.get('user_id')
    val = Password.query.filter_by(user_id=id).all()
    if val:
        return jsonify(data=val)
    return jsonify({'status_code': 404}) 

@main.route('/create_password', methods=['POST'])
def createPassword():      
    id= request.args.get('user_id')
    email_id= request.args.get('email')
    password= request.args.get('user_password')
    pass_title= request.args.get('title')
    new_entry_password= Password(email=email_id, user_id=id, user_password=password, title=pass_title)
    db.session.add(new_entry_password)
    db.session.commit()
    val= Password.query.filter_by(user_id=id).all()
    return jsonify(data=val)
