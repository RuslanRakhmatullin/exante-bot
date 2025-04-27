import logging
import requests
import os

def validate_signal(signal):
    required_fields = ["action", "ticker", "quantity"]
    return all(field in signal for field in required_fields)

def convert_ticker(ticker):
    # Simple example: add .NASDAQ instead of .US
    return ticker.replace(".US", ".NASDAQ")

def send_notification(message):
    # You can later expand this to send Telegram messages
    logging.info(f"Notification: {message}")
