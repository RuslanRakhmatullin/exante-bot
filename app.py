from flask import Flask, request, jsonify
import logging
from utils import validate_signal, convert_ticker, send_notification
from exante_client import place_order
from config import load_config

app = Flask(__name__)
load_config()


@app.route('/webhook', methods=['POST'])
def webhook():
    signal = request.json
    logging.info(f"Received signal: {signal}")

    # Validate signal
    if not validate_signal(signal):
        send_notification(f"Invalid signal received: {signal}")
        return jsonify({"error": "Invalid signal"}), 400

    # Ticker conversion
    exante_symbol = convert_ticker(signal['ticker'])
    signal['ticker'] = exante_symbol

    # Place order
    result = place_order(signal)

    if result['success']:
        send_notification(f"Order placed successfully: {signal}")
        return jsonify({"status": "Order placed"}), 200
    else:
        send_notification(f"Order failed: {result['error']}")
        return jsonify({"error": result['error']}), 500


if __name__ == '__main__':
    logging.basicConfig(filename='webhook.log', level=logging.INFO)
    app.run(host='0.0.0.0', port=5000)

