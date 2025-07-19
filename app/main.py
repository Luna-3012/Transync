import os
import glob
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from core.pipeline import run_full_pipeline
from config import LANGUAGE_OPTIONS
import base64

# --- Session state for navigation ---
if "page" not in st.session_state:
    st.session_state["page"] = "home"

# --- Home Page ---
if st.session_state["page"] == "home":
    st.markdown("<h1 style='text-align:center;'>Transync</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align:center;'>ᯓ★  Now Streaming in Every Language!  ★<span style=\"display:inline-block; transform: scaleX(-1);\">ᯓ</span></h3>", unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True) 
    url = st.text_input("📽️ Enter YouTube Video URL:")

    main_language = st.selectbox("🌐 Select language:", list(LANGUAGE_OPTIONS.keys()))
    dialects = LANGUAGE_OPTIONS[main_language]
    if len(dialects) > 1:
        region = st.selectbox("🗣 Select region/dialect", list(dialects.keys()))
        lang_code = dialects[region]
    else:
        lang_code = list(dialects.values())[0]

    if st.button("🚀 Start Translation") and url:
        st.session_state["url"] = url
        st.session_state["target_lang"] = lang_code
        st.session_state["page"] = "processing"
        st.rerun()

# --- Processing Page ---
elif st.session_state["page"] == "processing":
    file_path = "app/assets/happy_dance.gif"
    with open(file_path, "rb") as f:
        data = f.read()
        encoded = base64.b64encode(data).decode()

    st.markdown(
        f"""
        <div style="text-align:center">
            <img src="data:image/gif;base64,{encoded}" width="400"/>
        </div>
        """,
        unsafe_allow_html=True,
    )
    if "result" not in st.session_state:
        result = run_full_pipeline(st.session_state["url"], st.session_state["target_lang"])
        st.session_state["result"] = result
        st.session_state["page"] = "result"
        st.rerun()

# --- Result Page ---
elif st.session_state["page"] == "result":
    st.success("✅ Processing Done!")
    if st.session_state["result"].get("tts_warning"):
        st.warning(st.session_state["result"]["tts_warning"])
    st.subheader("🎬 Final Video")
    st.video(st.session_state["result"]["final_video"])

    preview_audio = st.toggle("Preview the translated audio?", value=False)
    if preview_audio:
        st.audio(st.session_state["result"].get("final_audio", ""))

    st.markdown(
        '<div style="margin-top: 0.5em; margin-bottom: 1.5em; color: #666; font-size: 1.1em;">'
        'Transcripts shown below for your reference — <b>download</b> as needed.'
        '</div>',
        unsafe_allow_html=True
    )

    st.subheader("📝 Original & Translated Transcript")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<b>Original Transcript</b>", unsafe_allow_html=True)
        original_text = st.session_state["result"].get("original_text", "")
        st.text_area(
            "",
            original_text,
            height=400,
            key="orig_text_area"
        )
        
        st.download_button(
            label="📥 Download Original Transcript",
            data=original_text,
            file_name="original_transcript.txt",
            mime="text/plain"
        )
    with col2:
        st.markdown("<b>Translated Transcript</b>", unsafe_allow_html=True)
        translated_text = st.session_state["result"]["translated_text"]
        st.text_area(
            "",
            translated_text,
            height=400,
            key="trans_text_area"
        )
        
        st.download_button(
            label="📥 Download Translated Transcript",
            data=translated_text,
            file_name="translated_transcript.txt",
            mime="text/plain"
        )

    if st.button("🔄 Start Over"):
        for folder in ["output", "downloads"]:
            for file in glob.glob(f"{folder}/*"):
                try:
                    os.remove(file)
                except Exception as e:
                    print(f"Error deleting {file}: {e}")
        for key in ["page", "url", "target_lang", "result"]:
            if key in st.session_state:
                del st.session_state[key]
        st.rerun()
