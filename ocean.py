import requests

def test_ocean(api_key):
    url = "https://api.ocean.io/v3/search/companies"

    headers = {
        "x-api-token": api_key,
        "Content-Type": "application/json"
    }

    payload = {
        "size": 5,
        "companiesFilters": {
            "includeDomains": [
                "microsoft.com"
            ]
        }
    }

    response = requests.post(
        url,
        headers=headers,
        json=payload
    )

    print("Status:", response.status_code)
    print(response.text[:1000])