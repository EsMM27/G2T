import openai
import random
import time

openai.api_key = 'key'
strings_list = []

with open('TTS_input_Ru.txt', 'r', encoding='utf-8') as file:
    for line in file:
        strings_list.append(line.strip())

filtered_strings = [text for text in strings_list if text.strip()]

def process_file(text):
    max_retries = 3  # Set the maximum number of retry attempts
    retry_delay = 5  # Set the delay between retry attempts
    timeout = 5  # Set a higher timeout value (in seconds)

    for _ in range(max_retries):
        try:
            completion = openai.chat.completions.create(
                model="gpt-4-0125-preview",
                messages=[
                    {"role": "system", "content": "You will be provided Russian Text, your task is to Translate it to english. DO NOT COMMENT JUST TRANSLATE. if you think you can phrase the translation better do it. The text could be a single phrase or an expression or a sentence, if unsure return a # along with the russian text"},
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

output_file_path = 'TTS_Input_GPT_3.5.txt'

with open(output_file_path, 'w', encoding='utf-8') as output_file:
    for index, text in enumerate(filtered_strings):
        completion_output = process_file(text)
        
        if completion_output is not None:
            print(completion_output)
            output_file.write(f'{index+10001}_{completion_output}\n')

print("All completions written to the file.")
import subprocess
subprocess.run(["python", "remove_quote.py"])


