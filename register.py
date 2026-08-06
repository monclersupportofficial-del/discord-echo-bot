import os
import requests

APPLICATION_ID = os.getenv("APPLICATION_ID")
TOKEN = os.getenv("DISCORD_TOKEN")
url = f"https://discord.com/api/v10/applications/{APPLICATION_ID}/commands"

command = {
    "name": "echo",
    "description": "Send a message as the app",
    "integration_types": [1],
    "contexts": [0, 1, 2],
    "options": [
        {
            "name": "message",
            "description": "Message to send",
            "type": 3,
            "required": True
        }
    ]
}


headers = {
    "Authorization": f"Bot {TOKEN}",
    "Content-Type": "application/json"
}

response = requests.post(url, json=command, headers=headers)

print(response.status_code)
print(response.text)
