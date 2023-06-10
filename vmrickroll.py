import requests
import os

def send_voice_message(channel_id, token):
    url = f"https://discord.com/api/v10/channels/{channel_id}/messages"

    headers = {
        "Authorization": token,
        'x-super-properties': 'eyJvcyI6IkFuZHJvaWQiLCJicm93c2VyIjoiRGlzY29yZCBBbmRyb2lkIiwiZGV2aWNlIjoiZHJlYW0ybHRla3MiLCJzeXN0ZW1fbG9jYWxlIjoiZnItRlIiLCJjbGllbnRfdmVyc2lvbiI6IjE3My4yMyAtIHJuIiwicmVsZWFzZV9jaGFubmVsIjoiZ29vZ2xlUmVsZWFzZSIsImRldmljZV92ZW5kb3JfaWQiOiI5M2RjMDRiOS04ODhkLTQ1NjMtYmI0OC1iMzA4NTNhYjNjOWMiLCJicm93c2VyX3VzZXJfYWdlbnQiOiIiLCJicm93c2VyX3ZlcnNpb24iOiIiLCJvc192ZXJzaW9uIjoiMjUiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjoxNzMwMjMsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGwsImRlc2lnbl9pZCI6MH0=',
        'user-agent': 'Discord-Android/173023;RNA',
        'content-type': 'application/json'
    }

    data = {
        "content": "",
        "channel_id": channel_id,
        "type": 0,
        "flags": 8192,
        "attachments": [
            {
                "id": 6,
                "filename": "voice-message.ogg",
                "uploaded_filename": "6bb1193e-7f1f-4bde-8054-503d401640ab/voice-message.ogg",
                "duration_secs": 212.04464583333333,
                "waveform": "KBkKDRAKGBIWcnZ+o1xub6GUX6CITm0b"
            }
        ]
        
    }

    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        print("Voice message sent successfully.")
    else:
        print("Failed to send voice message. Error:", response.text)

def get_token():
    print("Hello! Thanks for using my little rickroll script (never gonna give you up)")
    print("If this is your first time using it, you'll likely need to set a token (never gonna let you down)")
    print("You can get your account token by opening Discord in your browser, then pressing ctrl+shift+i (never gonna run around and desert you)")
    print("After that, click on the `network` tab and send a message anywhere in discord (never gonna make you cry)")
    print("You should see something appear on the network tab labled `message` or `messages` (never gonna say goodbye)")
    print("Click on that, then copy/paste everything after where it says `Authorization: ` into here (never gonna tell a lie and hurt you)")
    print("But before doing that, I would recommend that you or someone you trust carefully read through this script, just to be safe, as an account token can bypass any method of 2fa and give anyone full access to your account")
    print("BE CAREFUL OUT THERE! DON'T GIVE YOUR ACCOUNT TOKEN TO ANYONE/ANYTHING YOU DON'T TRUST\n\n")
    print("You'll also need the channel ID of the place you wanna rickroll. All you have to do for this is copy the channel link, then copy the second large number in the link, then paste it here.")
    print("Happy rickrolling!")
    token = input("After you have confirmed this script is safe, paste your token here: ")
    with open(".discordtoken/token.txt", 'w') as f:
        f.write(token)
    return token

if not os.path.exists(".discordtoken"):
    os.makedirs(".discordtoken")

try:
    with open(".discordtoken/token.txt") as f:
        token = f.read()
    if token is None:
        token = get_token()
except Exception:
    token = get_token()

channel_id = input("Channel ID: ")
send_voice_message(channel_id, token)
