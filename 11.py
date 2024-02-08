import time
from pathlib import Path
import requests

def prepare_request_data(input_text):
    """Prepare headers and data for the API request based on the length of input text."""
    headers = {
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": "key"
    }
    print("Length of input_text:", len(input_text))
    if len(input_text) <= 60:
        print("Using lower model")
        data = {
            "text": input_text,
            "model_id": "eleven_monolingual_v1",
            "voice_settings": {
                "stability": 0.45,
                "similarity_boost": 0.4,
                #"style": 0.3
            }
        }
    else:
        print("Using higher model")
        data = {
            "text": input_text,
            "model_id": "eleven_multilingual_v2",
            "voice_settings": {
                "stability": 0.55,
                "similarity_boost": 0.65,
                "style": 0.5
            }
        }

    return headers, data

# API endpoint for Eleven Labs Text-to-Speech
url = "https://api.elevenlabs.io/v1/text-to-speech/link"

# Folder containing speech file names (with .txt extension)
names_folder = Path("Russian_Text")

# Output folder for saving generated speech files
output_folder = Path("English_TTS")
output_folder.mkdir(exist_ok=True)

# Load file names from the folder
name_files = names_folder.glob("*.txt")
names = [file.stem + ".mp3" for file in name_files]  # Use .mp3 extension for Eleven Labs
    
# Read input file line by line
with open("TTS_Input_GPT_3.55.txt", "r", encoding="utf-8") as file:
    for i, line in enumerate(file):
        # Strip the prefix and use the line as input text
        input_text = line.split('_', 1)[-1].strip()
        print(input_text)

        # Choose the speech file path from the array
        speech_file_path = output_folder / names[i % len(names)]

        # Request speech generation from Eleven Labs API
        headers, data = prepare_request_data(input_text)
        response = requests.post(url, json=data, headers=headers)

        # Save generated speech to the specified file path with .mp3 extension
        with open(speech_file_path, 'wb') as f:
            f.write(response.content)

        print(f"Generated speech for line {i + 1} and saved to: {speech_file_path}")
        print("Sleeping for 0.2 seconds")
        time.sleep(0.2)

import subprocess
subprocess.run(["python", "mp3towav.py"])