import requests

RELAY_SERVER = "http://localhost:9000"

def connect_to_relay():
    try:
        response = requests.get(RELAY_SERVER)
        print("Connected to relay:", response.json())
    except Exception as e:
        print("Relay unavailable:", e)
