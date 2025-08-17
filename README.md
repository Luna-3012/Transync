# 🎙️ Transync: Multilingual Video Transcript Translator

This project enables translation of video audio into multiple languages. The tool performs the following:

1. Extracts audio from video files (e.g., `.mp4`)
2. Transcribes speech using automatic speech recognition (ASR)
3. Translates text into multiple languages
4. Converts translated text to speech
5. Allows download of the translated transcript (`.txt` format)

## 🎥 Demo

Watch the Transync in action: [Demo Video](https://drive.google.com/file/d/1kneRO7htXBkNkneh1-4b5QldAiWHfb_j/view?usp=sharing)

> 💡 Great for students, educators, content creators, or anyone building multilingual workflows.

---

## ⚙️ Features Implemented

- **Audio Extraction**: Extracts `.wav` audio from uploaded videos
- **Speech Recognition**: Uses Whisper (OpenAI) for accurate transcription
- **Transcript Generation**: Outputs original and translated text in plain `.txt` format
- **Multi-Language Support**: Supports translation into 130+ languages
- **Microsoft Azure Integration**: Uses Azure Translator and Text-to-Speech APIs
- **Transcript Downloads**: Download both original and translated transcripts

---

## 🛠️ Tech Stack

- **Python 3.10+** — The backbone of the entire project
- **Whisper ASR** — Powerful speech recognition by OpenAI
- **Microsoft Azure Translator Text API** — Accurate, scalable language translation
- **Microsoft Azure Text-to-Speech (TTS)** — Turns translated text into natural-sounding speech
- **FFmpeg** — Handles audio extraction and processing like a pro
- **Streamlit** — Builds an interactive and user-friendly web interface

---

## 🚀 How to Use

1. **Clone the repo:**
   ```bash
   git clone https://github.com/Luna-3012/Transync.git
   cd transync
   ```
   
2. **Create and activate virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set your Azure credentials in `.env`:**
   ```env
   AZURE_SPEECH_KEY=your_azure_speech_key
   AZURE_SPEECH_REGION=your_azure_speech_region

   AZURE_TRANSLATOR_KEY=your_translator_key
   AZURE_TRANSLATOR_REGION=your_translator_region
   AZURE_TRANSLATOR_ENDPOINT=your_translator_endpoint
   ```

5. **Run the Streamlit app:**
   ```bash
   streamlit run app/main.py
   ```

---

## 🔮 Future Scope
Here’s what’s cooking next:

- **SRT Subtitle Export** – Get subtitle files with proper timestamps
- **Video-Audio Sync** – Auto-match the speed of translated audio to original video duration
- **Context-aware Translation Chunks** – Smarter translation with better continuity
- **Speech Rate Tuning** – Dynamic rate adjustment for better flow

---

## 💬 Got Ideas? Questions?
I’d love to hear your feedback!
Whether it’s a bug, feature suggestion, or just a “hey, this is cool!” — feel free to open an issue or connect with me directly. 
Let’s make Transync even better, together!







