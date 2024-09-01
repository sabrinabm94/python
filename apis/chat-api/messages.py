import flask, json, jsonify
import datetime
import requests

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data for our catalog in the form of a list of dictionaries.
messages = [
    {
        'id': 1,
        'chat-room-id': 1,
        'message-text': 'oie',
        'sender-id': 1,
        'sender-username': 'Sabrina',
        'send-date': '02-07-2021-12:00',
        'receiver-username': 'Alex',
        'received': 'true',
        'receipt-date': '02-07-2021-12:01',
        'read': 'true',
        'reading-date': '02-07-2021-12:02'
    },
    {
        'id': 2,
        'chat-room-id': 1,
        'message-text': 'olá',
        'sender-id': 2,
        'sender-username': 'Alex',
        'send-date': '02-07-2021-12:03',
        'receiver-username': 'Alex',
        'received': 'True',
        'receipt-date': '02-07-2021-12:04',
        'read': 'false',
        'reading-date': 'null'
    },
]

newMessage = [
    {
        'id': 3,
        'chat-room-id': 1,
        'message-text': 'tudo bem?',
        'sender-id': 1,
        'sender-username': 'Sabrina',
        'send-date': '02-07-2021-12:04',
        'receiver-username': 'Alex',
        'received': 'false',
        'receipt-date': 'null',
        'read': 'false',
        'reading-date': 'null'
    }
]

chatRooms = [
    {
        'id': 1,
        'create-date': '02-07-2021-11:50',
        'creator-id': 1,
        'participants-id': [1, 2],
        'messages-number': 2
    },
    {
        'id': 2,
        'create-date': '01-07-2021-11:50',
        'creator-id': 4,
        'participants-id': [4, 5],
        'messages-number': 0
    }
]

chatRoom = [
    {
        'id': 1,
        'create-date': '02-07-2021-11:50',
        'creator-id': 1,
        'participants-id': [1, 2],
        'messages-number': 2
    }
]

newChatRoom = [
    {
        'id': 2,
        'create-date': '02-07-2021-13:00',
        'creator-id': 3,
        'participants-id': [3, 4, 5],
        'messages-number': 0
    }
]

#http://127.0.0.1:5000/
@app.route('/', methods=['GET'])
def home():
    return '''<h1>A simple Python api</h1><p>chat system api</p>'''

#http://127.0.0.1:5000/chat/chatroom/create
@app.route('/chat/chatroom/create', methods=['POST'])
def createChatRoom():
    #time = datetime.fromtimestamp(rt)
    return app.response_class(
        response=json.dumps(newChatRoom),
        status=200,
        mimetype='application/json'
    )

#http://127.0.0.1:5000/chat/chatroom/room/1
@app.route('/chat/chatroom/room/<int:id>', methods=['GET'])
def getChatRoom(id):
    if id:
        results = []

        for chatRoom in chatRooms:
            if chatRoom['id'] == id:
                results.append(chatRoom)

        return app.response_class(
            response=json.dumps(results),
            status=200,
            mimetype='application/json'
        )
    else:
        return "Error: No id field provided. Please specify an id."


#http://127.0.0.1:5000/chat/chatroom/user/1
@app.route('/chat/chatroom/user/<int:id>', methods=['GET'])
def getChatRoomByUserid(id):
    if id:
        results = []
        
        for chatRoom in chatRooms:
            if chatRoom['creator-id'] == id:
                results.append(chatRoom)

        return app.response_class(
            response=json.dumps(results),
            status=200,
            mimetype='application/json'
        )
    else:
        return "Error: No id field provided. Please specify an id."


#http://127.0.0.1:5000/chat/message/create
@app.route('/chat/message/create', methods=['POST'])
def createMessage():
    return app.response_class(
        response=json.dumps(newMessage),
        status=200,
        mimetype='application/json'
    )

#http://127.0.0.1:5000/chat/message/message/1
@app.route('/chat/message/message/<int:id>', methods=['GET'])
def getMessage(id):
    if id:
        results = []
        
        for message in messages:
            if message['chat-room-id'] == id:
                results.append(message)

        return app.response_class(
            response=json.dumps(results),
            status=200,
            mimetype='application/json'
        )
    else:
        return "Error: No id field provided. Please specify an id."

#http://127.0.0.1:5000/chat/message/all
@app.route('/chat/message/all', methods=['GET'])
def getAllMessages():
    return app.response_class(
        response=json.dumps(messages),
        status=200,
        mimetype='application/json'
    )

app.run()