from flask_restful import Resource
from models.continente import Continente


class ContinenteList(Resource):
    
    def get(self):
        return Continente.get_all(),200

