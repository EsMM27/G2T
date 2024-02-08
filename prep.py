import os
import shutil

def sort_and_index_wav_files(input_folder, output_folder):
    # Ensure the output folder exists or create it
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get a list of all .wav files in the input folder
    wav_files = [f for f in os.listdir(input_folder) if f.lower().endswith('.wav')]

    # Sort the files by size
    sorted_wav_files = sorted(wav_files, key=lambda f: os.path.getsize(os.path.join(input_folder, f)))

    # Index and copy the sorted files to the output folder
    for index, wav_file in enumerate(sorted_wav_files, start=100001):
        source_path = os.path.join(input_folder, wav_file)
        destination_name = f"{index:04d}_{wav_file}"
        destination_path = os.path.join(output_folder, destination_name)

        shutil.copyfile(source_path, destination_path)
        print(f"File '{wav_file}' copied to '{destination_path}'")

# Specify the input and output folders
input_folder_path = 'prep'
output_folder_path = 'Russian_Original'

# Call the function to sort and index .wav files
sort_and_index_wav_files(input_folder_path, output_folder_path)