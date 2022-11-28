import click
import requests
import logging
from os.path import exists

logger = logging.getLogger(__name__)

CREDENTIAL_PATH = '/tmp/codingdojo_credentials.json'

def init_token():
    global token
    token = None

def get_token():
    global token
    if (token):
        return token

    token = authenticate()
    return token

def load_creds():
    if not exists(CREDENTIAL_PATH):
        return None

    with open(CREDENTIAL_PATH, "r") as f:
        token = f.read()
        return token

def login():
    # Prompt the user for their credentials and request the token
    username = click.prompt('Username', type=str)
    password = click.prompt('Password', type=str, hide_input=True)

    response = requests.post(
        'https://dummyjson.com/auth/login',
        headers={'Content-Type': 'application/json'},
        json={
            'username': username,
            'password': password,
        },
    )
    response_json = response.json()
    if (response.status_code != 200):
        raise Exception(response_json["message"])
    return response_json["token"]

def authenticate():
    # Load the token if it exists, otherwise proceed to authenticate

    token = load_creds()
    if (token):
        return token

    token = login()
    with open(CREDENTIAL_PATH, "w+") as f:
        f.write(token)

    return token
