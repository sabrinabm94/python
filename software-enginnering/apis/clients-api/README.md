## Clients API

### Description

This REST API was created using **Flask** for managing client information.

### Installation

Steps to set up the project locally:

1. Clone the repository
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
   python main.py
   ```

2. Access the client listing:

   ```
   http://localhost:8080/api/v1.0/clients
   ```

### Requirements

Command instalation `pip install -r requirements.txt`

- Flask
- Flask-PyMongo
- bson
- flasgger
- requests
- jsonlib-python3
- werkzeug

### Testing

- Install [Insomnia](https://insomnia.rest/download) for API testing.
- Import `Insomnia-requests-api-clients.json` for testing the API requests.

### Author

Maintained by [Sabrina B.](https://github.com/sabrinabm94/about/blob/main/README.md).
Feel free to reach out at <sabrinabm94@gmail.com>.
