import os
import wave
import vosk
import json

# 获取当前文件所在目录（即子文件夹的路径）
current_dir = os.path.dirname(os.path.abspath(__file__))

# 设置语言模型路径
model_path = os.path.join(current_dir, "vosk-model-el-gr-0.7")  # 模型文件路径
audio_file = os.path.join(current_dir, "200_5.wav")  # 音频文件路径
output_file = os.path.join(current_dir, "transcription_200_5.txt")  # 输出文件路径

# 加载Vosk模型
if not os.path.exists(model_path):
    print("Please download the model from https://alphacephei.com/vosk/models and unpack as 'model' in the current folder.")
    exit(1)

# Initialize the model
model = vosk.Model(model_path)

# Open the audio file
wf = wave.open(audio_file, "rb")

# Check if audio format is supported
if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
    print("Audio file must be WAV format mono PCM.")
    exit(1)

# Initialize recognizer
recognizer = vosk.KaldiRecognizer(model, wf.getframerate())

# Process audio file and store partial results
transcriptions = []  # 用于存储所有部分识别结果
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

# 合并所有部分结果
full_transcription = " ".join(transcriptions)

# 将结果写入文本文档
with open(output_file, "w", encoding="utf-8") as f:
    f.write(full_transcription)

# 提示用户保存完成
print(f"Transcription saved to {output_file}")
