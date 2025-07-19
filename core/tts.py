import os
import azure.cognitiveservices.speech as speechsdk
from core.tts_voice_map import AZURE_TTS_VOICES, LANG_CODE_TO_NAME

SPEECH_KEY = os.getenv("AZURE_SPEECH_KEY")
SPEECH_REGION = os.getenv("AZURE_SPEECH_REGION")

def generate_tts(text: str, lang_code: str, output_path: str, gender: str = "female", voice_name: str = None):
    if not SPEECH_KEY or not SPEECH_REGION:
        raise ValueError("Missing Azure credentials. Set AZURE_SPEECH_KEY and AZURE_SPEECH_REGION environment variables.")

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    speech_config = speechsdk.SpeechConfig(subscription=SPEECH_KEY, region=SPEECH_REGION)

    gender = gender.lower()
    language_name = LANG_CODE_TO_NAME.get(lang_code, lang_code)
    warning_message = None
    
    if voice_name:
        speech_config.speech_synthesis_voice_name = voice_name
    elif lang_code in AZURE_TTS_VOICES:
        # Check if the requested gender is available
        if gender in AZURE_TTS_VOICES[lang_code]:
            speech_config.speech_synthesis_voice_name = AZURE_TTS_VOICES[lang_code][gender]
            selected_voice = AZURE_TTS_VOICES[lang_code][gender]
        else:
            available_genders = list(AZURE_TTS_VOICES[lang_code].keys())
            if available_genders:
                fallback_gender = available_genders[0]  
                selected_voice = AZURE_TTS_VOICES[lang_code][fallback_gender]
                warning_message = f"Oops! No {gender} voice for {language_name} — but hey, we've got a {fallback_gender} voice ready to roll! 🎧"
                print(warning_message)
            else:
                raise ValueError(f"No voices available for language '{language_name}'.")
    else:
        raise ValueError(f"No valid voice found for language '{language_name}' and gender '{gender}'.")
    speech_config.speech_synthesis_voice_name = selected_voice

    audio_config = speechsdk.audio.AudioOutputConfig(filename=output_path)
    synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

    result = synthesizer.speak_text_async(text).get()

    if result.reason != speechsdk.ResultReason.SynthesizingAudioCompleted:
        if result.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = result.cancellation_details
            print("TTS Canceled: ", cancellation_details.reason)
            print("Error Details: ", cancellation_details.error_details)
            raise RuntimeError(f"TTS synthesis failed: {cancellation_details.reason} - {cancellation_details.error_details}")
        else:
            raise RuntimeError(f"TTS synthesis failed: {result.reason}")
    else:
        print(f"✅ TTS audio saved to: {output_path}")
        return {"output_path": output_path, "warning": warning_message}
