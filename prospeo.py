import requests

def test_prospeo(api_key):
    headers = {
        "X-KEY": api_key
    }

    print("Prospeo key loaded:", bool(api_key))