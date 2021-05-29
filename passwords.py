from enum import unique
from logging import error
import re
from flask import request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


from main import  db , app ,ma


 
class passwords (db.Model):
    id = db.Column(db.Integer , primary_key = True , unique = True)
    title  = db.Column(db.String(100))
    email = db.Column(db.String(100) )
    user_password = db.Column(db.String(100))
    user_id = db.Column(db.Integer)

    def __init__(self , email , user_password , user_id ,title ) :
        self.email  = email
        self.user_password = user_password 
        self.user_id = user_id
        self.title = title

   
class passwordSchema(ma.Schema):
    class Meta:
        fields = ('id','email','user_password' , 'user_id' , 'title')

passwordschema = passwordSchema()
passwordschema = passwordSchema(many=True)


@app.route('/get_password' ,methods = ['GET'] )
def showPasswords():
     
    id = request.args.get('user_id')
    

    val = passwords.query.filter_by(user_id =  id ).first()
    if val :
        passwordSchema(val)
        return passwordschema.jsonify(val)
    
    return 404 


@app.route('/' ,methods = ['GET'] )
def showPasswords():
      
    # id = request.args.get('user_id')
    # email_id = request.args.get('email')
    # password = request.args.get('user_password')
    # pass_title = request.args.get('title')

    # new_entry_password = passwords(email=email_id , user_id= id , user_password=password , title = pass_title)
    # db.session.add(new_entry_password)
    # db.session.commit()

    # val = passwords.query.filter_by(user_id =  id ).first()
    
    #passwordSchema(val)
    #return passwordSchema().jsonify(val)
    return '<h1>kritik</h1>'