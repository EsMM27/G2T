import os

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

os.chdir("working dir")
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
