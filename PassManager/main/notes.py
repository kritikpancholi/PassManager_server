from flask import Flask, request, jsonify, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask import request, jsonify
from PassManager.models import Note, User, Password
from PassManager import db , ma

notes_blueprint = Blueprint('notes_blueprint', __name__)


class NoteSchema(ma.Schema):
    class Meta:
        fields = ("title", "description" , "user_id" ,"id")


note_schema = NoteSchema()
notes_schema = NoteSchema(many=True)

@notes_blueprint.route('/get_note', methods=['GET'])
def showNote():
    id = request.args.get('user_id')
    val = Note.query.filter_by(user_id=id).all()
    if val:
        return jsonify(notes_schema.dump(val))
    return 'No Data',400


@notes_blueprint.route('/create_note', methods=['POST' , 'GET'])
def createNote():      
    id= request.json.get('user_id')
    note_description = request.json.get('description')
    note_title= request.json.get('title')
    if  note_title== '' :
        return 'Note not added ', 400
    new_entry_note= Note(user_id=id, title=note_title, description = note_description) 
    db.session.add(new_entry_note)
    db.session.commit()
    val= Note.query.filter_by(user_id = id).all()

    return jsonify(notes_schema.dump(val))

@notes_blueprint.route('/delete_note/<id_to_delete>',methods = ['DELETE'])
def delete_note(id_to_delete):
   
    val = Note.query.filter_by(id = id_to_delete).first()
    db.session.delete(val)
    db.session.commit()

    return 'Deleted' , 200

