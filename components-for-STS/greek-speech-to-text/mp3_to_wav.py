from pydub import AudioSegment
import os

# Get the current directory where the script is located
current_dir = os.path.dirname(os.path.abspath(__file__))

# Prompt user for the input file name (without the file extension)
input_filename = input("Please enter the name of the MP3 file (without extension): ")

# MP3 file path
audio_file = os.path.join(current_dir, f'audio/{input_filename}.mp3')

# Export file path
export_file = os.path.join(current_dir, f'audio/{input_filename}.wav')

# Load the MP3 file
audio = AudioSegment.from_mp3(audio_file)

# Convert to mono
audio = audio.set_channels(1)

# Ensure the WAV file is exported in PCM format
audio.export(export_file, format="wav", codec="pcm_s16le")

print(f'Conversion complete! The WAV file is saved as {export_file}')
