import streamlit as st
import pyttsx3
import tempfile
import os

st.title('文章読み上げソフト')

text_input = st.text_area('文章を入力してください')

if st.button('結果を表示'):
    st.write('入力結果: ', text_input)

    engine = pyttsx3.init()
    with tempfile.NamedTemporaryFile(delete=False, suffix='.wav') as tmp_file:
        temp_path = tmp_file.name
    engine.save_to_file(text_input, temp_path)
    engine.runAndWait()

    audio_file = open(temp_path, 'rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio/wav')    

    st.download_button(
        label="音声をダウンロード",
        data=audio_bytes,
        file_name="読み上げ.wav",
        mime="audio/wav"
    )

    audio_file.close()
    os.remove(temp_path)
