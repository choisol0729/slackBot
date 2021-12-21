import json
import requests
import time
from datetime import datetime

slack_token = "qx3hFhFFoXv8QVwvNsa3kBK2"
channel_id = "C01C2M6D0D6"

def main():
    while(True):
        time.sleep(1)
        if datetime.now().strftime("%H:%M:%S") == "18:00:00" or datetime.now().strftime("%H:%M:%S") == "19:00:00" or datetime.now().strftime("%H:%M:%S") == "10:30:00":
            data = json.dumps({'Content-Type': 'application/x-www-form-urlencoded',
                                'Authorization': slack_token,
                                'channel': channel_id, 
                                'text': "It's time to go home!"
                                })
            print("It's time to go home!")
            URL = "https://slack.com/api/chat.postMessage"
            res = requests.post(URL, data=data)
            print(res)
            print(data)
        else:
            print(datetime.now().strftime("%H:%M:%S"))

main()