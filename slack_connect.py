'''
TODO:  

Implement a queue

Source derived from: https://gist.github.com/Rits1272/f9374043be1b7b1421b8c08678655c54
Author credit: https://gist.github.com/Rits1272
'''

from slack import RTMClient
import requests

import os
import subprocess
import shlex
import threading

def youtube_download_func(url):
    command = f"yt-dlp {url}"

    # determine OS type
    posix = False
    if os.name == 'posix':
        posix = True

    if posix: # posix case, single command string including arguments
        args = [command]
    else: # windows case, split arguments by spaces
        args = shlex.split(command)
    p = subprocess.Popen(args, start_new_session=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL )
  
@RTMClient.run_on(event="message")
def amusebot(**payload):
    """
    This function triggers when someone sends
    a message on the slack
    """
    data = payload["data"]
    web_client = payload["web_client"]
    bot_id = data.get("bot_id", "")

    # If a message is not send by the bot
    if bot_id == "":
        channel_id = data["channel"]

        # Extracting message send by the user on the slack
        text = data.get("text", "")
        parameter = text.split()

        response = ""

        #usage: youtube http://youtube.com/watch?v=sample_id
        if "youtube" in text.lower():
            user = data.get("user", "")

            url_parameter = text.split("|")[-1].strip()
            final_url = url_parameter.replace('>', '')
            final_url = final_url.replace('<', '')

            parameters = final_url.split()
            response = f"Added {parameters[1]} to my youtube queue"

            function_parameter = parameters[1]
            youtube_thread = threading.Thread(target=youtube_download_func, args=(function_parameter,))
            youtube_thread.start()

            # Sending message back to slack
            web_client.chat_postMessage(channel=channel_id, text=response)

        elif "whoami" in text.lower():
            user = data.get("user", "")
            response = f"I am slack based download bot"
            # Sending message back to slack
            web_client.chat_postMessage(channel=channel_id, text=response)
        elif "help" in text.lower():
            user = data.get("user", "")
            response = f"Sample help command"
            # Sending message back to slack
            web_client.chat_postMessage(channel=channel_id, text=response)
try:
    rtm_client = RTMClient(token="YOUR-TOKEN-HERE")
    print("Bot is up and running!")
    rtm_client.start()
except Exception as err:
    print(err)
