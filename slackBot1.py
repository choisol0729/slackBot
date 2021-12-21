import logging
import time
from datetime import datetime
# Import WebClient from Python SDK (github.com/slackapi/python-slack-sdk)
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# WebClient instantiates a client that can call API methods
# When using Bolt, you can use either `app.client` or the `client` passed to listeners.
client = WebClient(token="xoxb-1386872335970-2866213462595-G5zQEkGD9Gd4beqAbvmLjQ6u")
logger = logging.getLogger(__name__)
# ID of the channel you want to send the message to
channel_id = "C01C2M6D0D6"

while(True):
    time.sleep(1)
    nowtime = datetime.now().strftime("%H:%M:%S")
    if nowtime == "18:00:00" or nowtime == "19:00:00":
        try:
            # Call the chat.postMessage method using the WebClient
            result = client.chat_postMessage(
                channel=channel_id, 
                text="It's time to go home~! \U0001f600\U0001f600"
            )
            logger.info(result)
        except SlackApiError as e:
            logger.error(f"Error posting message: {e}")
    elif nowtime == "12:30:00":
        try:
            # Call the chat.postMessage method using the WebClient
            result = client.chat_postMessage(
                channel=channel_id, 
                text="Lunch Time!"
            )
            logger.info(result)
        except SlackApiError as e:
            logger.error(f"Error posting message: {e}")
    print(nowtime)