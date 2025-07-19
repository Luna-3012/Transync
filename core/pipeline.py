import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np
import soundfile as sf

from core import (
    tts,
    whisper_transcribe,
    translate,
    audio_tools,
    gender_detection,  
)
from utils import file_io, text_utils, video_utils


def run_full_pipeline(video_input, target_lang):
    print("🔁 Starting pipeline...")

    # Download video
    if isinstance(video_input, str):
        print("📥 Downloading video...")
        input_path = file_io.download_youtube_video(video_input)
    else:
        input_path = file_io.save_uploaded_file(video_input)
    print(f"📁 Video ready at: {input_path}")

    # Extract & separate audio
    audio_path = audio_tools.extract_audio(input_path)
    vocals, background = audio_tools.separate_audio(audio_path)
    print("🎙️ Separated vocals and background.")

    # Transcribe + Detect language
    transcript, detected_lang, segments = whisper_transcribe.transcribe(vocals)
    print(f"📝 Transcribed. Language: {detected_lang}")

    # Grammar correction
    corrected = text_utils.correct_text(transcript, lang_code=detected_lang)

    # Translation
    translated = translate.translate_text(corrected, target_lang)
    print("🌍 Translated text.")

    # Detect speaker gender
    gender = gender_detection.detect_gender(vocals)
    print(f"🧠 Detected speaker gender: {gender}")

    # TTS
    output_path = "output/translated_voice.wav"
    tts_result = tts.generate_tts(translated, lang_code=target_lang, output_path=output_path, gender=gender)
    print("🔊 TTS generated.")

    tts_warning = None
    if isinstance(tts_result, dict) and tts_result.get("warning"):
        tts_warning = tts_result["warning"]

    # Merge audio
    final_audio = audio_tools.mix_audio(output_path, background)
    print("🎛️ Mixed audio with background.")

    # Replace in video
    final_video = video_utils.replace_audio(input_path, final_audio)
    print(f"🎬 Final video ready at: {final_video}")

    return {
        "final_video": final_video,
        "translated_text": translated,
        "original_text": transcript,
        "tts_warning": tts_warning,
        "final_audio": final_audio
    }
