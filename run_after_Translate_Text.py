import re

def has_cyrillic(text):
    return bool(re.search('[\u0400-\u04FF]', text))

def main(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        for line_number, line in enumerate(file, start=1):
            if has_cyrillic(line):
                print(f"Line {line_number}: {line.strip()}")

if __name__ == "__main__":
    file_path = "TTS_Input_GPT_3.5.txt"  # Replace with the path to your text file
    main(file_path)