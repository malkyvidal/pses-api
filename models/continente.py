from db import db

class Continente(db.Model):
    __tablename__ = 'continentes'
    id = db.Column(db.Integer,primary_key = True)
    nombre = db.Column(db.String(20))

    def __init__(self,nombre):
        self.nombre = nombre
    
    
    def json(self):
        return {'id':self.id,'nombre':self.nombre}


    @classmethod
    def get_all(cls):
        continentes = [c.json() for c in  cls.query.all()]
        return {'continentes': continentes}