import requests
import os
import shutil

text_file = []

input_file_path = 'TTS_Input_GPT_3.5.txt'  # Replace with the actual path to your input text file
output_file_path = 'TTS_Input_GPT_3.5_ready.txt'  # Replace with the desired path for the output file

with open(input_file_path, 'r', encoding='utf-8') as input_file:
    lines = input_file.readlines()

# Remove the first 5 characters from each line
modified_lines = [line.split('_', 1)[1] for line in lines]

# Write the modified lines to the output file
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    output_file.writelines(modified_lines)

print("First 5 characters removed and saved to:", output_file_path)

####################################################################################
####################################################################################

def read_lines_to_array(file_path):
    lines_array = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            lines_array.append(line.strip())
    return lines_array

def main():
    file_path = 'TTS_Input_GPT_3.5_ready.txt'  # Replace with the actual path to your text file

    lines_array = read_lines_to_array(file_path)

    # Print or do something with the lines_array
    for line in lines_array:
        text_file.append(line)
main()



for string in text_file:
    print(string)

for iteration, text in enumerate(text_file, start=1):
    # Make a POST request for each string
    response = requests.post("http://127.0.0.1:7860/run/generate", json={"data": [text, "hello world", "None", "/n", "hero1", {"name": "audio.wav", "data": "data:audio/wav;base64,UklGRiQAAABXQVZFZm10IBAAAAABAAEARKwAAIhYAQACABAAZGF0YQAAAAA="}, 0, 2, 0, 2, 40, 0.3, "P", 8, 0, 0.8, 0.8, 3, 3, 2, ["Conditioning-Free"], False, False]}).json()
    
    # Extract the "data" field from the response
    data = response["data"]

    # Process the data as needed
    # ...

    # Optionally, print or do something with the processed data
    print(f"Processed data for input '{text}'DONE! {iteration}/{len(text_file)}")
    
def copy_every_second_file(input_folder, output_folder):
    # Ensure the output folder exists, create it if not
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get a list of all files in the input folder
    files = [f for f in os.listdir(input_folder) if os.path.isfile(os.path.join(input_folder, f))]

    # Copy every second file to the output folder and rename with "index_name"
    for i in range(1, len(files), 2):
        file_to_copy = files[i]
        source_path = os.path.join(input_folder, file_to_copy)
    
        # Format the new file name as "{index}_{original_name}"
        new_file_name = f"{i // 2 + 103001}_{file_to_copy}"
    
        destination_path = os.path.join(output_folder, new_file_name)
        shutil.copyfile(source_path, destination_path)
        print(f"Copied and renamed: {new_file_name}")

# Provide the paths for the input and output folders
input_folder_path = ''
output_folder_path = 'English_TTS'

# Call the function to copy every second file with formatting
copy_every_second_file(input_folder_path, output_folder_path)

#############################################################################################
#############################################################################################

def delete_all_files(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                os.rmdir(file_path)
        except Exception as e:
            print(f"Error deleting {file_path}: {e}")

# Replace 'your_folder_path' with the actual path of the folder containing the files you want to delete
folder_path = ''

delete_all_files(folder_path)
print("cache deleted")

##############################################################################################
##############################################################################################

    