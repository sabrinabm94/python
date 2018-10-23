#importar o framework flask
from flask import Flask, jsonify, request
from client import Client
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://172.18.0.35:27017/DBsabrina"
mongo = PyMongo(app)

#listClients = [
#    Client(name="Sabrina", email="sabrinabgbc@email.com", phone="5547000000000"),
#    Client(name="Alexander", email="callfrygou@email.com", phone="5547000000000")
#]

@app.route('/api/v1.0/clients', methods=['GET'])
def get_tasks():
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
def create_client():
    newcli = Client()
    newcli._id = ObjectId()
    newcli.name = request.json['name']
    newcli.email = request.json['email']
    newcli.phone = request.json['phone']

    ret = mongo.db.clients.insert_one(newcli.__dict__).inserted_id
    return jsonify({'id': str(ret)}), 201


#config

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)

#acesso padrão: http://localhost:5000/api
#acesso modificado: http://localhost:8080/api
#acesso versionado: http://localhost:8080/api/v1.0/clients
