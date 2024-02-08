import os
import shutil
import concurrent.futures
import numpy as np
from pydub import AudioSegment
from pyworld import dio, stonemask

def calculate_pitch(audio_array, frame_period, frame_rate):
    f0, timeaxis = dio(audio_array.astype(np.float64), frame_rate, frame_period=frame_period)
    f0 = stonemask(audio_array.astype(np.float64), f0, timeaxis, frame_rate)
    return f0

def is_ai_generated(audio_file_path, std_threshold, pitch_threshold, frame_period):
    try:
        audio = AudioSegment.from_file(audio_file_path)
        audio_array = np.array(audio.get_array_of_samples())
        std_deviation = np.std(audio_array)
        pitch_values = calculate_pitch(audio_array, frame_period=frame_period, frame_rate=audio.frame_rate)
        return std_deviation < std_threshold and np.max(np.abs(np.diff(pitch_values))) > pitch_threshold
    except FileNotFoundError:
        print(f"File not found: {audio_file_path}")
        return False
    except Exception as e:
        print(f"Error processing {audio_file_path}: {e}")
        return False

def process_and_move_files(input_folder, output_folder, std_threshold, pitch_threshold, frame_period, match_folder, move_folder):
    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Process multiple files in parallel
    with concurrent.futures.ProcessPoolExecutor() as executor:
        futures = []
        for filename in os.listdir(input_folder):
            file_path = os.path.join(input_folder, filename)
            futures.append(executor.submit(process_file, file_path, std_threshold, pitch_threshold, frame_period, output_folder))

        # Wait for all tasks to complete
        concurrent.futures.wait(futures)

    # Match and move files
    match_and_move_files(match_folder, output_folder, move_folder)

def process_file(file_path, std_threshold, pitch_threshold, frame_period, output_folder):
    if is_ai_generated(file_path, std_threshold, pitch_threshold, frame_period):
        new_file_path = os.path.join(output_folder, os.path.basename(file_path))
        shutil.copy2(file_path, new_file_path)
        print(f"Copied AI-generated file: {file_path} to {new_file_path}")
    else:
        print(f"Non AI-generated file: {file_path}")

def match_and_move_files(folder_a, folder_b, folder_c):
    os.makedirs(folder_c, exist_ok=True)
    prefixes_b = {filename.split('_')[0] for filename in os.listdir(folder_b)}

    for filename_a in os.listdir(folder_a):
        prefix_a = filename_a.split('_')[0]
        if prefix_a in prefixes_b:
            file_path_a = os.path.join(folder_a, filename_a)
            file_path_c = os.path.join(folder_c, filename_a)
            shutil.copy2(file_path_a, file_path_c)
            print(f"Moved file from {file_path_a} to {file_path_c}")

if __name__ == '__main__':
    input_folder = 'English_TTS'
    output_folder = 'DISTORTED'
    std_threshold = 4000
    pitch_threshold = 230
    frame_period = 1
    match_folder = 'Russian_Text'
    move_folder = 'DISTORTED_match'

    process_and_move_files(input_folder, output_folder, std_threshold, pitch_threshold, frame_period, match_folder, move_folder)
    
