import os
import wave
import vosk
import json

# Get the current directory where the script is located
current_dir = os.path.dirname(os.path.abspath(__file__))

# Prompt user for the input WAV file name (without extension)
input_filename = input("Enter the name of the WAV file (without extension): ")

# Set paths for the model, audio file, and output file
model_path = os.path.join(current_dir, "vosk-model-el-gr-0.7")  # Path to the model
audio_file = os.path.join(current_dir,  f"audio/{input_filename}.wav")  # Path to the audio file
output_file = os.path.join(current_dir, f"transcriptions/{input_filename}_transcription.txt")  # Output file path

# Load Vosk model
if not os.path.exists(model_path):
    print("Please download the model from https://alphacephei.com/vosk/models and unpack it as 'vosk-model' in the current folder.")
    exit(1)

# Initialize the model
model = vosk.Model(model_path)

# Open the audio file
wf = wave.open(audio_file, "rb")

# Check if the audio format is supported
if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
    print("Audio file must be in WAV format, mono, and PCM encoding.")
    exit(1)

# Initialize recognizer
recognizer = vosk.KaldiRecognizer(model, wf.getframerate())

# Process the audio file and store partial results
transcriptions = []  # List to store all partial transcription results
while True:
    data = wf.readframes(4000)
    if len(data) == 0:
        break
    if recognizer.AcceptWaveform(data):
        partial_result = recognizer.Result()
        transcriptions.append(json.loads(partial_result).get("text", ""))

# Get the final result
final_result = json.loads(recognizer.FinalResult()).get("text", "")
transcriptions.append(final_result)

# Combine all partial results
full_transcription = " ".join(transcriptions)

# Write the transcription to a text file
with open(output_file, "w", encoding="utf-8") as f:
    f.write(full_transcription)

# Notify the user that the transcription has been saved
print(f"Transcription saved to {output_file}")
