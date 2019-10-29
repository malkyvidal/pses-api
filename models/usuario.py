from db import db

class Usuario(db.Model):
    __tablename__ = "usuarios"

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(30))
    password = db.Column(db.String(30))


    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def json(self):
        return {"id":self.id, "username":self.username, "password":self.password}
    
    @classmethod
    def find_user_by_name(cls,name):
        user = cls.query.filter_by(username = name).first()
        return user 
    
    @classmethod
    def find_user_by_id(cls,id):
        user = cls.query.filter_by(id = id).first()
        return user 
