import requests

API_KEY = "814babe0220c02f68e4245aa40e83b64751ec29587af5592f606c0ca304614ed"
ENDPOINT = "https://127.0.0.1:27124"
"""
curl -X 'GET' \
  'https://127.0.0.1:27124/active/' \
  -H 'accept: text/markdown' \
  -H 'Authorization: Bearer 814babe0220c02f68e4245aa40e83b64751ec29587af5592f606c0ca304614ed'
"""

response = requests.get(
    ENDPOINT + "/active/",
    headers={"accept": "text/markdown", "Authorization": "Bearer " + API_KEY},
)

print(response.text)
