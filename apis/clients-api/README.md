# Clients API

## Description

This REST API was created using Flask and is used for managing client information.

## Requirements

### Create a Virtual Environment

```bash
python -m venv env

# For Linux
source env/bin/activate

# For Windows
env\Scripts\activate
```

### Install Packages

#### One by One

```bash
pip install Flask flask-pymongo bson flasgger requests jsonlib-python3 werkzeug
```

#### Using the Requirements File

Create a `requirements.txt` file with the following content and install all packages at once:

```
Flask
flask-pymongo
bson
flasgger
requests
jsonlib-python3
werkzeug
```

Then, run:

```bash
pip install -r requirements.txt
```

### Verify Installed Packages

```bash
pip freeze
```

### Uninstall Packages

```bash
pip uninstall Flask
```

### Upgrade Packages

To upgrade Flask to a specific version:

```bash
pip install --upgrade Flask==2.0.2
```

## Running the Application

1. **Run the Python Script**

   Execute the main Python script to start the Flask server:

   ```bash
   python main.py
   ```

   This will start the Flask application on `http://localhost:8080`.

2. **View the Client Listing**

   Open your web browser and navigate to:

   ```
   http://localhost:8080/api/v1.0/clients
   ```

   This URL will display the list of clients in JSON format.

## Testing

### Requirements

To test the requests, install [Insomnia](https://insomnia.rest/download).

### Usage

Import the `Insomnia-requests-api-clients.json` file into Insomnia and test the available requests.

## Contacts

Sabrina B.  
Email: <sabrinabm94@gmail.com>
