## Chat API

### Description

This REST API was created using **Flask** for managing chat rooms and messages between users.

### Installation

Steps to set up the project locally:

1. Clone the repository.
2. Create a virtual environment:

   ```bash
   python -m venv env
   ```

3. Activate the environment:
   - For Linux: `source env/bin/activate`
   - For Windows: `env\Scripts\activate`

4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### Usage

1. Run the Flask server:

   ```bash
   python messages.py
   ```

2. Access the following endpoints:

   - **Home Page**: `http://127.0.0.1:5000/`
   - **Create Chat Room**: `POST http://127.0.0.1:5000/chat/chatroom/create`
   - **Get Chat Room by ID**: `GET http://127.0.0.1:5000/chat/chatroom/room/<int:id>`
   - **Get Chat Room by User ID**: `GET http://127.0.0.1:5000/chat/chatroom/user/<int:id>`
   - **Create Message**: `POST http://127.0.0.1:5000/chat/message/create`
   - **Get Messages by Chat Room ID**: `GET http://127.0.0.1:5000/chat/message/message/<int:id>`
   - **Get All Messages**: `GET http://127.0.0.1:5000/chat/message/all`

### Requirements

- Flask
- json

### Testing

- Install [Insomnia](https://insomnia.rest/download) for API testing.
- Test the endpoints by making requests to the provided URLs.

### Author

Maintained by [Sabrina B.](https://github.com/sabrinabm94/about/blob/main/README.md).
Feel free to reach out at <sabrinabm94@gmail.com>.
