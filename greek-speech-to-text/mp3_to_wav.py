from pydub import AudioSegment
import os

# 获取当前文件所在目录（即子文件夹的路径）
current_dir = os.path.dirname(os.path.abspath(__file__))

# MP3 文件路径
audio_file = os.path.join(current_dir, '200_5.mp3')

export_file = os.path.join(current_dir, '200_5.wav')

# 加载 MP3 文件
audio = AudioSegment.from_mp3(audio_file)

# 转换为单声道
audio = audio.set_channels(1)

# 确保使用 PCM 格式导出为 WAV 文件
audio.export(export_file, format="wav", codec="pcm_s16le")
