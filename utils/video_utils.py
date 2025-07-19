import ffmpeg
import os

def replace_audio(video_path, audio_path):
    output_path = "output/final_video.mp4"
    os.makedirs("output", exist_ok=True)

    print(f"Replacing audio in video: {video_path}")
    print(f"Using audio file: {audio_path}")
    print(f"Output will be: {output_path}")

    try:
        video_input = ffmpeg.input(video_path)
        audio_input = ffmpeg.input(audio_path)

        ffmpeg.output(
            video_input['v'],     
            audio_input['a'],     
            output_path,
            vcodec='copy',        
            acodec='aac',         
            ac=1,                 
            ar=44100,            
            strict='experimental'
        ).run(overwrite_output=True)

        print(f"✅ Video replacement completed: {output_path}")
        print(f"📦 File size: {os.path.getsize(output_path)} bytes")

        return output_path

    except Exception as e:
        print(f"Failed to replace audio: {e}")
        raise e
