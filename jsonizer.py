import os
import re
import json

def parse_text_file(file_path):
    with open(file_path, 'r', encoding='cp1251') as file:
        lines = file.readlines()

    quests = {}
    current_quest = None
    current_dialogue = None

    for line in lines:
        # Detect quest names
        quest_match = re.match(r'^\s{3}(.+)$', line)
        if quest_match:
            quest_name = quest_match.group(1)
            quests[quest_name] = {"NPC": [], "HERO": []}  # Change to initialize HERO as a list
            current_quest = quest_name
            continue

        # Detect dialogues
        dialogue_match = re.match(r'^\[(.+?)\]\s+"(.+)"$', line)
        if dialogue_match:
            dialogue_id = dialogue_match.group(1)
            dialogue_text = dialogue_match.group(2)
            quests[current_quest]["NPC"].append({"id": dialogue_id, "text": dialogue_text})
            continue

        # Detect hero items
        hero_item_match = re.match(r'^\s{1}\[(.+?)\]\s+"(.+)"$', line)
        if hero_item_match:
            hero_item_id = hero_item_match.group(1)
            hero_item_text = hero_item_match.group(2)
            quests[current_quest]["HERO"].append({"id": hero_item_id, "text": hero_item_text})
            continue

    return quests

def save_to_json(data, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    txt_files_folder = "txtFiles"  # Assuming your text files are located in a folder named 'txtFiles'
    json_files_folder = "JSON"  # Assuming you want to save JSON files in a folder named 'JSON'

    # List all files in the txtFiles folder
    txt_files = os.listdir(txt_files_folder)

    if txt_files:  # Check if there are any text files in the folder
        # Take the first file in the list
        first_txt_file = os.path.join(txt_files_folder, txt_files[0])

        # Remove the ".txt" extension from the file name
        temp = first_txt_file[:-4]

        # Generate the path for the corresponding JSON file in the JSON folder
        json_file_path = os.path.join(json_files_folder, f"{os.path.basename(temp)}.json")

        # Parse the text file and save the data to JSON
        quests_data = parse_text_file(first_txt_file)  # Fix: Replace "txt_file_path" with "first_txt_file"
        save_to_json(quests_data, json_file_path)
    else:
        print("No text files found in the folder.")