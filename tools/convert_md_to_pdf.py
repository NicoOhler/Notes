import requests

API_KEY = "814babe0220c02f68e4245aa40e83b64751ec29587af5592f606c0ca304614ed"
ENDPOINT = "https://127.0.0.1:27124"

response = requests.get(
    ENDPOINT + "/commands/",
    headers={"accept": "text/markdown", "Authorization": "Bearer " + API_KEY},
    verify=False,  # disable SSL verification
)

print(response.text)


response = requests.put(
    ENDPOINT + "/commands/",
    headers={"accept": "text/markdown", "Authorization": "Bearer " + API_KEY},
    verify=False,  # disable SSL verification
    json={
        "command": "list-changed-files",
        "repo": "