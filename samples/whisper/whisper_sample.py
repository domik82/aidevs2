# source aidevs forum: https://pastebin.com/raw/qsArBwW2

# dependencies install:
# pip install requests
# pip install termcolor
# pip install git+https://github.com/openai/whisper.git
# by Nondzu 2023.11 github.com/Nondzu

# to run create a .env file and fill it with API_KEY=your_api_key
#  API_KEY = "put your api key here"

# It might be required to run:
# pip install git+https://github.com/openai/whisper.git

import os
import requests
import json
import whisper
from termcolor import colored

#load env
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv('OPENAI_API_KEY')

def get_token_from_api():
    """Retrieve token from the API."""
    url = 'https://zadania.aidevs.pl/token/whisper'
    headers = {'Content-Type': 'application/json'}
    data = {'apikey': API_KEY}
    response = requests.post(url, headers=headers, data=json.dumps(data))
    return response.json()['token']

def get_task_from_api(token):
    """Retrieve task from the API using a token."""
    url = f'https://zadania.aidevs.pl/task/{token}'
    response = requests.get(url)
    return response.json()

def download_mp3_from_url(url, filename="downloaded_file.mp3"):
    """Download an MP3 file from a given URL."""
    response = requests.get(url)
    with open(filename, 'wb') as f:
        f.write(response.content)

def transcribe_audio_file(filename):
    """Use WHISPER to transcribe a given audio file."""
    model = whisper.load_model("large-v2")
    result = model.transcribe(filename)
    return result["text"]

def send_answer_to_api(token, answer):
    """Send transcribed answer back to the API."""
    data = {'answer': answer}
    headers = {'Content-Type': 'application/json'}
    url = f'https://zadania.aidevs.pl/answer/{token}'
    response = requests.post(url, headers=headers, data=json.dumps(data))
    return response.json()

if __name__ == "__main__":
    token = get_token_from_api()
    task = get_task_from_api(token)

    print(colored("Received Task:", "yellow"))
    print(colored(json.dumps(task, indent=4), "cyan"))

    mp3_url = task['msg'].split(' ')[-1]
    print(colored(f"Downloading MP3 from: {mp3_url}", "green"))
    download_mp3_from_url(mp3_url, "mateusz.mp3")

    print(colored("Transcribing audio file...", "green"))
    transcribed_text = transcribe_audio_file("mateusz.mp3")
    print(colored(f"Transcribed Text: {transcribed_text}", "cyan"))

    print(colored("Sending answer to API...", "green"))
    response = send_answer_to_api(token, transcribed_text)
    print(colored(f"API Response: {json.dumps(response, indent=4)}", "cyan"))