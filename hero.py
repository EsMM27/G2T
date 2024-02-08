import os
import subprocess

def process_files_in_batches(input_folder, output_folder, batch_size=500):
    try:
        # Ensure the input folder exists
        if not os.path.exists(input_folder):
            raise FileNotFoundError(f"Input folder '{input_folder}' not found.")

        files = [f for f in os.listdir(input_folder) if os.path.isfile(os.path.join(input_folder, f))]

        # Create the output folder if it doesn't exist
        os.makedirs(output_folder, exist_ok=True)

        # Split files into batches
        file_batches = [files[i:i + batch_size] for i in range(0, len(files), batch_size)]

        # Process each batch
        for batch in file_batches:
            # Change working directory
            os.chdir(input_folder)

            # Construct the command to transcribe multiple files at once
            command = [
                "whisper",
                *batch,
                "--output_dir", output_folder,
                "--model", "large-v3",
                "--language", "ru",
                "--task", "transcribe",
                "--output_format", "txt"
            ]

            # Run the command
            subprocess.run(command)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Specify your input and output folder paths and batch size
    input_folder = "workingdir"
    output_folder = "workingdir"
    batch_size = 500

    # Process files in batches
    process_files_in_batches(input_folder, output_folder, batch_size)