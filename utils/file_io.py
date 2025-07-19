import os
import uuid
from yt_dlp import YoutubeDL

DOWNLOADS_DIR = "downloads"

def save_uploaded_file(uploaded_file):
    os.makedirs(DOWNLOADS_DIR, exist_ok=True)
    file_path = os.path.join(DOWNLOADS_DIR, f"{uuid.uuid4()}.mp4")
    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())
    return file_path

def download_youtube_video(url):
    """Download YouTube video and return the file path"""
    os.makedirs(DOWNLOADS_DIR, exist_ok=True)
    file_path = os.path.join(DOWNLOADS_DIR, f"{uuid.uuid4()}.mp4")
    
    ydl_opts = {
        'format': 'best[ext=mp4]/best',
        'outtmpl': file_path,
        'quiet': True,
        'nocheckcertificate': True,
        'ignoreerrors': False,
        'no_warnings': True,
        'http_headers': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-us,en;q=0.5',
            'Sec-Fetch-Mode': 'navigate',
        },
        'extractor_args': {
            'youtube': {
                'skip': ['dash', 'hls'],
            }
        }
    }
    
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    
    return file_path
