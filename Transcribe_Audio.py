# Python script to create and run a batch file

import os
import subprocess

# Folder containing files
folder_path = "Russian_Original"
folder_path2 = "Russian_Original2"

# Output folder for transcribed text
output_folder = "" #USE FULL PATH example C:\\Users\\JohnDoe\\OneDrive\\Russian_Text

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Get a list of all files in the folder
files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
files2 = [f for f in os.listdir(folder_path2) if os.path.isfile(os.path.join(folder_path2, f))]
print()

os.chdir("") ##FULL PATH FOR DIRECTORY Russian_Original example C:\\Users\\JohnDoe\\OneDrive\\Russian_Original

# Construct the command to transcribe multiple files at once
command = [
    "whisper",
    *files,  # Include all file names as separate arguments
    "--output_dir", output_folder,
    "--model", "large-v3",#tiny,base,medium,large
    "--language", "ru",#language
    "--task", "transcribe",#transcribe/translate
    "--output_format", "txt"
]
command2 = [
    "whisper",
    *files2,  # Include all file names as separate arguments
    "--output_dir", output_folder,
    "--model", "large-v3",#tiny,base,medium,large
    "--language", "ru",#language
    "--task", "transcribe",#transcribe/translate
    "--output_format", "txt"
]

# Run the command
import subprocess
subprocess.run(command)
os.chdir("")
subprocess.run(command2)


###############################################################################################################
###############################################################################################################

# Function to read contents of a file
def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content
os.chdir("")
# Folder containing text files
folder_path = 'Russian_Text'

# Output file to store all contents
output_file_path = 'TTS_input_Ru.txt'

# Get a list of all text files in the folder
text_files = [f for f in os.listdir(folder_path) if f.endswith('.txt')]

# Open the output file in write mode with utf-8 encoding
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    # Loop through each text file starting from 1 and write its content to the output file
    for file_name in text_files:
        file_path = os.path.join(folder_path, file_name)
        content = read_file(file_path)
        transformed_text = content.replace('\n', ' ')
        print(content)
        output_file.write(transformed_text + "\n")

print(f"Contents of all text files in '{folder_path}' written to '{output_file_path}'.")

subprocess.run(["python", "Translate_GPT.py"])