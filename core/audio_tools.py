import os
from pydub import AudioSegment

OUTPUT_DIR = "output"

def extract_audio(video_path):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    output_path = os.path.join(OUTPUT_DIR, "audio.wav")
    AudioSegment.from_file(video_path).export(output_path, format="wav")
    return output_path

def separate_audio(audio_path):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    vocals = os.path.join(OUTPUT_DIR, "vocals.wav")
    background = os.path.join(OUTPUT_DIR, "background.wav")
    
    audio = AudioSegment.from_file(audio_path)
    audio.export(vocals, format="wav")
    
    # Create a silent background track
    silent_bg = AudioSegment.silent(duration=len(audio))
    silent_bg.export(background, format="wav")
    
    return vocals, background

def mix_audio(vocals_path, background_path):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    vocals = AudioSegment.from_file(vocals_path)
    background = AudioSegment.from_file(background_path)
    mixed = vocals.overlay(background)
    final_path = os.path.join(OUTPUT_DIR, "final_audio.wav")
    mixed.export(final_path, format="wav")
    return final_path
