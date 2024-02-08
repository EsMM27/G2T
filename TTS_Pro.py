
from pathlib import Path
from openai import OpenAI
import time

# Initialize OpenAI client
client = OpenAI()

# Input text file path
input_file_path = "TTS_Input_GPT_3.5.txt"

# Folder containing speech file names (with .txt extension)
names_folder = Path("Russian_Text")

# Output folder for saving generated speech files
output_folder = Path("English_TTS")
output_folder.mkdir(exist_ok=True)

# Load file names from the folder
name_files = names_folder.glob("*.txt")
names = [file.stem + ".wav" for file in name_files]  # Use .wav extension

# Read input file line by line
with open(input_file_path, "r", encoding="utf-8") as file:
    for i, line in enumerate(file):
        # Strip the prefix and use the line as input text
        input_text = line.split('_', 1)[-1].strip()
        
        # Choose the speech file path from the array
        speech_file_path = output_folder / names[i % len(names)]
        
        # Generate speech using OpenAI API
        response = client.audio.speech.create(
            model="tts-1",
            voice="alloy",
            input=input_text
        )

        # Save generated speech to the specified file path with .wav extension
        response.stream_to_file(speech_file_path)

        print(f"Generated speech for line {i + 1} and saved to: {speech_file_path}")
        print("sleeping for 1.2 seconds")
        time.sleep(1.2)
        