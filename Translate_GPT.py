import openai
import json
import time
import os

with open("credentials.json", "r", encoding="utf-8") as json_file:
    cred = json.load(json_file)

key = cred["API_KEY"][0]["GPT_API"]

openai.api_key = '{key}'
strings_dict = {}

json_folder = "JSON"  # Assuming your text files are located in a folder named 'txtFiles'
file = os.listdir(json_folder)
first_txt_file = os.path.join(json_folder, file[0])

with open(first_txt_file, 'r', encoding='utf-8') as file:
    strings_dict = json.load(file)

def process_text(text):
    max_retries = 3
    retry_delay = 5
    timeout = 5

    for _ in range(max_retries):
        try:
            completion = openai.chat.completions.create(
                model="gpt-4-0125-preview",
                messages=[
                    {"role": "system", "content": "Translate the following text from Russian to English:"},
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

for key, value in strings_dict.items():
    for role, items in value.items():  # Iterate over NPC and HERO dictionaries
        for item in items:  # Iterate over the list of dictionaries
            print("Current item:", item)  # Print out the current item for inspection
            text = item.get('text')  # Use item.get() method to avoid KeyError
            translated_text = process_text(text)
            if translated_text is not None:
                item['text'] = translated_text

# Write back the translated texts to the JSON file
with open('output.json', 'w', encoding='utf-8') as output_file:
    json.dump(strings_dict, output_file, ensure_ascii=False, indent=4)

print("Translation completed and saved in output.json.")