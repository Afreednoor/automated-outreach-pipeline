import requests
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("PROSPEO_API_KEY")

headers = {
    "X-KEY": api_key,
    "Content-Type": "application/json"
}

payload = {
    "page": 1,
    "filters": {
        "company": {
            "names": {
                "include": ["Microsoft"]
            }
        }
    }
}

response = requests.post(
    "https://api.prospeo.io/search-person",
    headers=headers,
    json=payload
)

print("Status:", response.status_code)
print(response.text[:1000])