import time
from pathlib import Path
import requests
import json

def prepare_request_data(input_text):
    """Prepare headers and data for the API request based on the length of input text."""
    headers = {
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": "{eleven_labs_key}"
    }
    print("Length of input_text:", len(input_text))

    print("Using higher model")
    data = {
            "text": input_text,
            "model_id": "eleven_multilingual_v2",
            "voice_settings": {
                "stability": 0.6,
                "similarity_boost": 0.65,
                "style": 0.2,
                "use_speaker_boost": True
            }
        }

    return headers, data

# API endpoints for Eleven Labs Text-to-Speech
urlHero = "https://api.elevenlabs.io/v1/text-to-speech/edOqtUYFs1EZnhw99Up1"

urlNPC = "https://api.elevenlabs.io/v1/text-to-speech/Dver0N51vKNEmES6uUL0"

# Output folder for saving generated speech files
output_folder = Path("English_TTS")
output_folder.mkdir(exist_ok=True)

with open("credentials.json", "r", encoding="utf-8") as json_file:
    cred = json.load(json_file)

eleven_labs_key = cred["API_KEY"][0]["ELEVEN_LABS"]

# Load JSON data from file
with open("output.json", "r", encoding="utf-8") as json_file:
    data = json.load(json_file)


# Iterate over entries in the JSON file
for key, value in data.items():
    for role, entries in value.items():
        # Select the appropriate URL based on the role
        if role == "HERO":
            url = urlHero
        elif role == "NPC":
            url = urlNPC
        else:
            raise ValueError(f"Invalid role: {role}")

        for entry in entries:
            input_text = entry.get("text", "").strip()
            print(input_text)

            # Choose the speech file path
            speech_file_path = output_folder / f"{role}_{entry['id']}.mp3"

            # Request speech generation from Eleven Labs API
            headers, request_data = prepare_request_data(input_text)
            response = requests.post(url, json=request_data, headers=headers)

            # Save generated speech to the specified file path with .mp3 extension
            with open(speech_file_path, 'wb') as f:
                f.write(response.content)

            print(f"Generated speech for {role} and saved to: {speech_file_path}")
            print("Sleeping for 0.2 seconds")
            time.sleep(0.2)