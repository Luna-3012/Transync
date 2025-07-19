import parselmouth
import numpy as np

def detect_gender(audio_path):
    try:
        snd = parselmouth.Sound(audio_path)
        pitch = snd.to_pitch()
        pitch_values = pitch.selected_array['frequency']
        pitch_values = pitch_values[pitch_values != 0]  

        if len(pitch_values) == 0:
            return "unknown"

        avg_pitch = np.mean(pitch_values)

        # Simple threshold-based classification
        if avg_pitch < 165:
            return "male"
        elif avg_pitch >= 165:
            return "female"
        else:
            return "unknown"
    except Exception as e:
        print(f"[ERROR] Gender detection failed: {e}")
        return "unknown"
