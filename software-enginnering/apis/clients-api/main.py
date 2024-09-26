from flask import Flask, jsonify, request, redirect
from bson.objectid import ObjectId
from flasgger import Swagger, swag_from

app = Flask(__name__)
swagger = Swagger(app)

# Mock de banco de dados
clients = [
    {'_id': '1', 'name': "Sabrina", 'email': "sabrinabgbc@email.com", 'phone': "5547000000000"},
    {'_id': '2', 'name': "Alexander", 'email': "callfrygou@email.com", 'phone': "5547000000000"}
]

mock_db = {
    'clients': clients
}

@app.route('/')
def index():
    return redirect("/swagger-ui/")

@app.route('/api/v1.0/clients', methods=['GET'])
@swag_from({
    'summary': 'Retrieve a list of clients',
    'responses': {
        200: {
            'description': 'A list of clients',
            'schema': {
                'type': 'object',
                'properties': {
                    'clients': {
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'properties': {
                                '_id': {'type': 'string'},
                                'name': {'type': 'string'},
                                'email': {'type': 'string'},
                                'phone': {'type': 'string'}
                            }
                        }
                    }
                }
            }
        }
    }
})
def get_client():
    return jsonify({'clients': mock_db['clients']}), 200

@app.route('/api/v1.0/clients/<string:_id>', methods=['GET'])
@swag_from({
    'summary': 'Retrieve a client by ID',
    'parameters': [
        {
            'name': '_id',
            'in': 'path',
            'type': 'string',
            'required': True,
            'description': 'The ID of the client to retrieve'
        }
    ],
    'responses': {
        200: {
            'description': 'Client details',
            'schema': {
                'type': 'object',
                'properties': {
                    '_id': {'type': 'string'},
                    'name': {'type': 'string'},
                    'email': {'type': 'string'},
                    'phone': {'type': 'string'}
                }
            }
        },
        404: {
            'description': 'Client not found'
        }
    }
})
def get_client_by_id(_id):
    for client in mock_db['clients']:
        if client['_id'] == _id:
            return jsonify(client), 200
    return jsonify({'message': 'Client not found'}), 404

@app.route('/api/v1.0/clients', methods=['POST'])
@swag_from({
    'summary': 'Create a new client',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'name': {'type': 'string'},
                    'email': {'type': 'string'},
                    'phone': {'type': 'string'},
                    '_id': {'type': 'string'}
                }
            }
        }
    ],
    'responses': {
        201: {
            'description': 'The ID of the created client',
            'schema': {
                'type': 'object',
                'properties': {
                    '_id': {'type': 'string'}
                }
            }
        },
        500: {
            'description': 'Internal error'
        }
    }
})
def create_client():
    client_id = request.json.get('_id', str(ObjectId()))  # Use provided ID or generate new one
    new_client = {
        '_id': client_id,
        'name': request.json.get('name'),
        'email': request.json.get('email'),
        'phone': request.json.get('phone')
    }
    mock_db['clients'].append(new_client)
    return jsonify({'_id': new_client['_id']}), 201

@app.route('/api/v1.0/clients/<string:_id>', methods=['PUT'])
@swag_from({
    'summary': 'Update an existing client',
    'parameters': [
        {
            'name': '_id',
            'in': 'path',
            'type': 'string',
            'required': True,
            'description': 'The ID of the client to update'
        },
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'name': {'type': 'string'},
                    'email': {'type': 'string'},
                    'phone': {'type': 'string'}
                }
            }
        }
    ],
    'responses': {
        200: {
            'description': 'The ID of the updated client',
            'schema': {
                'type': 'object',
                'properties': {
                    '_id': {'type': 'string'}
                }
            }
        },
        404: {
            'description': 'Client not found'
        },
        500: {
            'description': 'Internal error'
        }
    }
})
def update_client(_id):
    for client in mock_db['clients']:
        if client['_id'] == _id:
            client.update(request.json)
            return jsonify({'_id': _id}), 200
    return jsonify({'message': 'Client not found'}), 404

@app.route('/api/v1.0/clients/<string:_id>', methods=['DELETE'])
@swag_from({
    'summary': 'Delete a client',
    'parameters': [
        {
            'name': '_id',
            'in': 'path',
            'type': 'string',
            'required': True,
            'description': 'The ID of the client to delete'
        }
    ],
    'responses': {
        200: {
            'description': 'The count of deleted clients',
            'schema': {
                'type': 'object',
                'properties': {
                    'deleted_count': {'type': 'integer'}
                }
            }
        },
        404: {
            'description': 'Client not found'
        },
        500: {
            'description': 'Internal error'
        }
    }
})
def delete_client(_id):
    global mock_db
    initial_count = len(mock_db['clients'])
    # Crie uma nova lista de clientes excluindo o cliente com o ID fornecido
    new_clients_list = [client for client in mock_db['clients'] if client['_id'] != _id]
    # Verifique se algum cliente foi excluído
    deleted_count = initial_count - len(new_clients_list)
    mock_db['clients'] = new_clients_list  # Atualize a lista no banco de dados mock
    return jsonify({'deleted_count': deleted_count}), 200 if deleted_count > 0 else 404

# Configuração
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)

#acesso padrão: http://localhost:5000/api
#acesso modificado: http://localhost:8080/api
#acesso ao swagger: http://localhost:8080/swagger/ui/

#Get clients http://localhost:8080/api/v1.0/clients
