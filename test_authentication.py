import requests
import os
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth

# Load environment variables from .env
load_dotenv()

# Read credentials
CLIENT_ID = os.getenv('EXANTE_CLIENT_ID')
CLIENT_SECRET = os.getenv('EXANTE_CLIENT_SECRET')


def test_exante_auth():
    url = 'https://api-demo.exante.eu/oauth2/token'

    payload = {
        'grant_type': 'client_credentials'
    }

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    try:
        response = requests.post(
            url,
            data=payload,
            headers=headers,  # <-- add the proper header
            auth=HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET)
        )
        response.raise_for_status()
        data = response.json()

        if 'access_token' in data:
            print("Authentication successful!")
            print(f"Access Token: {data['access_token'][:20]}... (truncated)")
        else:
            print("Authentication failed! No access token returned.")
            print(data)

    except Exception as e:
        print(f"Error during authentication: {e}")


if __name__ == "__main__":
    test_exante_auth()



