from flask import Flask 
from flask_restful import  Api 
from resources.continente import ContinenteList
from resources.pais import PaisesPorContinente
from resources.capital import CapitalPorPais
from flask_jwt import JWT,jwt_required 
from security import authenticate, identity

app =   Flask(__name__)

app.secret_key = 'clave'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:malky@localhost:5432/paises'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #para usar solo el tracker de sqlalchemy y no el de flask-sqlalchemy
api = Api(app)

 

jwt = JWT(app,authenticate,identity) 



#api.add_resource(Pais,'/pais/<string:name>')
api.add_resource(ContinenteList,'/todosloscontinentes')
api.add_resource(PaisesPorContinente,'/continente/<int:continenteid>/paises')
api.add_resource(CapitalPorPais,'/pais/<int:paisid>/capital')





if __name__=="__main__":
    from db import db 
    db.init_app(app)
    app.run(port=5000)


