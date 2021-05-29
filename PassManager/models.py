from PassManager import db

class User (db.Model):
    '''
        User model is the model that takes id, email and password
    '''
    id= db.Column(db.Integer, primary_key = True)
    email= db.Column(db.String(100), unique = True)
    password= db.Column(db.String)
 
    def __init__(self, email, password):
        self.email= email
        self.password= password


class Password (db.Model):
    '''
        Password model takes in title, email, user password and user id
    '''
    id= db.Column(db.Integer, primary_key= True, unique= True)
    title= db.Column(db.String(100)) 
    email= db.Column(db.String(100))
    user_password= db.Column(db.String(100))
    user_id= db.Column(db.Integer)

    def __init__(self, email, user_password, user_id, title):
        self.email= email
        self.user_password= user_password 
        self.user_id= user_id
        self.title= title
