import requests

url = "https://api.boxberry.ru/json.php"

payload = "{\r\n  \"token\": \"1aa280094920f222075d35c5b252a0c8e\",\r\n  \"method\": \"ParcelInfo\",\r\n  \"parcels\": [\r\n    {\r\n      \"track\": \"AJD164610941\"\r\n    }\r\n  ]\r\n}"
headers = {}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)