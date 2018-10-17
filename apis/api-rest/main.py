#importar o framework flask
from flask import Flask, jsonify
from client import Client
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["mongodb://192.168.106.44:27017/DBwaltercoan"]
mongo = PyMongo(app)

listClients = [
    Client(name="Sabrina", email="sabrinabgbc@email.com", phone="5547000000000"),
    Client(name="Alexander", email="callfrygou@email.com", phone="5547000000000")
]

@app.route('/api/v1.0/client', methods=['GET'])
def get_tasks():
    return jsonify({'clients': [umcli.__dict__ for umcli in listClients]})
#expressão lambda do python

#código principal
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)

#acesso padrão: http://localhost:5000/api
#acesso modificado: http://localhost/api
#acesso versionado: http://localhost/api/v1.0/client
