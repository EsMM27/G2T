import os
import shutil

def replace_file_names(folder_a, folder_b):
    # Get the list of file names from folder A
    files_a = os.listdir(folder_a)

    # Iterate over the files in folder B
    for file_b in os.listdir(folder_b):
        # Get the full path of the file in folder B
        file_b_path = os.path.join(folder_b, file_b)

        # Check if the item is a file
        if os.path.isfile(file_b_path):
            # Get the corresponding file name from folder A
            file_a_name = files_a.pop(0)

            # Build the full path for the file in folder A
            file_a_path = os.path.join(folder_a, file_a_name)

            # Replace the file name in folder B with the name from folder A
            os.rename(file_b_path, os.path.join(folder_b, file_a_name))

            print(f"Replaced {file_b} with {file_a_name}")

# Replace with your folder paths
folder_a_path = "Russian_Text"
folder_b_path = "English_TTS"

replace_file_names(folder_a_path, folder_b_path)