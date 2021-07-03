#importar o frameworks do flask
from flask import Flask, jsonify, request, redirect
from client import Client
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask_swag import Swag

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://172.18.0.35:27017/DBsabrina"
mongo = PyMongo(app)
swag = Swag(app)
app.config['SWAG_TITLE'] = "API CLIENTES"
app.config['SWAG_API_VERSION'] = "1.0"

@app.route('/')
def index():
    return redirect("/swagger/ui")

#listClients = [
#    Client(name="Sabrina", email="sabrinabgbc@email.com", phone="5547000000000"),
#    Client(name="Alexander", email="callfrygou@email.com", phone="5547000000000")
#]

@app.route('/api/v1.0/clients', methods=['GET'])

#documentação da api via swager
@swag.mark.summary("objetivo deste metodo é retornar uma lista de clientes")
@swag.mark.response(201, "Lista de Usuários")

def get_client():
    clients = []
    for client in mongo.db.clients.find():
        newClient = Client()
        newClient._id = str(client['_id'])
        newClient.name = str(client['name'])
        newClient.phone = str(client['phone'])
        newClient.email = str(client['email'])
        clients.append(newClient)
    return jsonify({'clients': [client.__dict__ for client in clients]}), 201

@app.route('/api/v1.0/clients', methods=['POST'])
@swag.mark.simple_param('body', 'Client object', str)
@swag.mark.response(201, "Retorn_Id document")
@swag.mark.response(500, "Internal error")

def create_client():
    newcli = Client()
    newcli._id = ObjectId()
    newcli.name = request.json['name']
    newcli.email = request.json['email']
    newcli.phone = request.json['phone']

    ret = mongo.db.clients.insert_one(newcli.__dict__).inserted_id
    return jsonify({'id': str(ret)}), 201

@app.route('/api/v1.0/clients/<string:_id>', methods=['PUT'])
#cria documentação socinha pois já informamos o que seria buscado pela declaração da rota
def update_client(_id):
    updatecli = Client()
    updatecli._id = ObjectId(_id)
    updatecli.name = request.json['name']
    updatecli.email = request.json['email']
    updatecli.phone = request.json['phone']
    mongo.db.clients.update_one({'_id':updatecli._id}, {'$set':updatecli.__dict__}, upsert=False)
    return jsonify({'id':str(updatecli._id)}), 201

@app.route('/api/v1.0/clients/<string:_id>', methods=['DELETE'])
def delete_client(_id):
    _id = ObjectId(_id)
    ret = mongo.db.clients.delete_one(('_id:id')).deleted_count
    return jsonify({'deleted_count': str(ret)}), 201

#config
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)

#acesso padrão: http://localhost:5000/api
#acesso modificado: http://localhost:8080/api
#acesso versionado: http://localhost:8080/api/v1.0/clients
#acesso ao swagger: http://localhost:8080/swagger/ui/
