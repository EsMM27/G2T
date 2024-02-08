input_file_path = "TTS_Input_GPT_3.5.txt"  # Replace with your input file path
output_file_path = "TTS_Input_GPT_3.55.txt"  # Replace with your desired output file path

# Read content from the input file
with open(input_file_path, "r", encoding='utf-8' ) as input_file:
    content_before = input_file.read()

# Count the number of characters before removing double quotes
char_count_before = len(content_before)

# Remove double quotes from the content
cleaned_content = content_before.replace('"', '')

# Count the number of characters after removing double quotes
char_count_after = len(cleaned_content)

# Write the cleaned content to the output file
with open(output_file_path, "w",  encoding='utf-8') as output_file:
    output_file.write(cleaned_content)

print("Character count before:", char_count_before)
print("Character count after:", char_count_after)
print("Processing complete. Result written to:", output_file_path)