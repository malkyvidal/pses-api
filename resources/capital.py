from flask_restful import Resource
from models.pais import Pais 
from flask_jwt import jwt_required 

class CapitalPorPais(Resource):
    @jwt_required() 
    def get(self, paisid):
        pais = Pais.find_Pais_by_id(paisid)
        if pais:
            return pais.json(),200
        return {'message':'no encontrado'},404