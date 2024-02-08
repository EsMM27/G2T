from pydub import AudioSegment
import os

def convert_mp3_to_wav(mp3_file, wav_file):
    sound = AudioSegment.from_mp3(mp3_file)
    sound.export(wav_file, format="wav")

def convert_all_mp3_to_wav_and_delete(mp3_folder_path):
    for filename in os.listdir(mp3_folder_path):
        if filename.endswith(".mp3"):
            mp3_file_path = os.path.join(mp3_folder_path, filename)
            wav_file_path = os.path.join(mp3_folder_path, os.path.splitext(filename)[0] + ".wav")
            
            convert_mp3_to_wav(mp3_file_path, wav_file_path)
            
            # Delete the MP3 file after conversion
            os.remove(mp3_file_path)
            
            print(f"Converted and Deleted: {filename}")

# Provide the path to the folder containing MP3 files
mp3_folder_path = "English_TTS"

# Call the function to convert all MP3 files to WAV and delete them
convert_all_mp3_to_wav_and_delete(mp3_folder_path)

