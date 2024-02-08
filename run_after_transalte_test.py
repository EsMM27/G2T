import os
import re

def has_cyrillic(text):
    return bool(re.search('[\u0400-\u04FF]', text))

def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        for line_number, line in enumerate(file, start=1):
            if has_cyrillic(line):
                print(f"File: {file_path}, Line {line_number}: {line.strip()}")

def main(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            process_file(file_path)

if __name__ == "__main__":
    folder_path = "your_folder_path"  # Replace with the path to your folder containing .txt files
    main(folder_path)