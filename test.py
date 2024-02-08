import os
import openai
import random
import time

openai.api_key = 'aikey'
input_folder = 'Russian_Text'
output_folder = 'English_Text'  # Add the folder path where you want to save the output

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

def read_text_files(folder_path):
    texts = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                text = file.read().strip()
                if text:
                    texts.append((filename, text))
    return texts

def process_file(text):
    max_retries = 3  # Set the maximum number of retry attempts
    retry_delay = 5  # Set the delay between retry attempts
    timeout = 5  # Set a higher timeout value (in seconds)

    for _ in range(max_retries):
        try:
            completion = openai.chat.completions.create(
                model="gpt-3.5-turbo-1106",
                messages=[
                    {"role": "system", "content": "You will translate russian text into english text, do not comment on anything just translate"},
                    {"role": "user", "content": text}
                ],
                timeout=timeout
            )
            output = completion.choices[0].message.content
            return output
        except Exception as e:
            print(f"Error processing input '{text}': {e}")
            time.sleep(retry_delay)
            continue

    print(f"Maximum retries reached for input: {text}")
    return None

# Read texts from the input folder
input_texts = read_text_files(input_folder)

for filename, text in input_texts:
    output_file_path = os.path.join(output_folder, f'{filename}')

    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        completion_output = process_file(text)
        
        if completion_output is not None:
            print(completion_output)
            output_file.write(f'{completion_output}\n')

print("All completions written to the files.")