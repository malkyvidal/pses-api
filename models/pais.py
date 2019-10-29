from db import db

class Pais(db.Model):
    __tablename__= 'paises'
    id = db.Column(db.Integer,primary_key = True)
    nombre = db.Column(db.String(100))
    capital = db.Column(db.String(100))
    id_cont = db.Column(db.Integer)


    def json(self):
        return {'id': self.id,'nombre':self.nombre,'capital':self.capital}
    
    @classmethod
    def find_by_continente(cls,id_cont):
        paises = [ p.json() for p  in   cls.query.filter_by(id_cont =  id_cont).all()]
        return paises


    @classmethod
    def find_Pais_by_id(cls,id):
        pais = cls.query.filter_by(id = id).first()
        return pais

    def __init__(self,nombre, capital, id_cont):
        self.nombre = nombre
        self.capital = capital
        self.id_cont = id_cont