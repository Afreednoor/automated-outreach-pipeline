import requests

def test_brevo(api_key):
    headers = {
        "accept": "application/json",
        "api-key": api_key
    }

    response = requests.get(
        "https://api.brevo.com/v3/account",
        headers=headers
    )

    data = response.json()

    print("Company:", data.get("companyName"))
    print("Email:", data.get("email"))