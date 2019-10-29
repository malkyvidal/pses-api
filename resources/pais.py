from flask_restful import Resource
from models.pais import Pais 




class PaisesPorContinente(Resource):

    def get(self, continenteid):
        return Pais.find_by_continente(continenteid),200



