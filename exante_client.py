import requests
import os

def get_access_token():
    payload = {
        'grant_type': 'client_credentials',
        'client_id': os.getenv('EXANTE_CLIENT_ID'),
        'client_secret': os.getenv('EXANTE_CLIENT_SECRET')
    }
    response = requests.post('https://api-live.exante.eu/oauth2/token', data=payload)
    return response.json()['access_token']

def place_order(signal):
    try:
        access_token = get_access_token()
        url = f"{os.getenv('EXANTE_API_URL')}/trade"

        headers = {
            'Authorization': f"Bearer {access_token}",
            'Content-Type': 'application/json'
        }

        order_data = {
            "account_id": os.getenv('EXANTE_APPLICATION_ID'),
            "instrument_id": signal['ticker'],
            "side": signal['action'],  # buy or sell
            "quantity": signal['quantity'],
            "order_type": "market" if not signal.get('price') else "limit",
            "price": signal.get('price', None)
        }

        response = requests.post(url, headers=headers, json=order_data)
        if response.status_code == 200:
            return {"success": True}
        else:
            return {"success": False, "error": response.text}
    except Exception as e:
        return {"success": False, "error": str(e)}
