import streamlit as st
from pydub import AudioSegment, silence
import speech_recognition as sr
import os

recog = sr.Recognizer()

#Global Variables:
text_list = ""
final_result= ""

#Pydub: A library used to play with Audio files
st.set_page_config(layout="wide")
st.markdown("""<h1 style = 'text-align: center; color : red;'>
            Audio To Text Converter App
            </h1>             
            """ , unsafe_allow_html=True)
st.markdown("---" , unsafe_allow_html=True)


formats = ["mp3" , "wav"]
rec_audio = st.file_uploader("Upload Your Audio File:")
#Spliting This Audio File into Segments
if rec_audio:
    st.audio(rec_audio)
    audio_segment = AudioSegment.from_file(rec_audio)
    chunks = silence.split_on_silence(audio_segment , min_silence_len=500 , silence_thresh=audio_segment.dBFS-20 , keep_silence=100)
    print("The recieve Audio is : " , rec_audio)
    print("The Segmented Audio is: " , audio_segment)
    print("The Type of Audio is : " , type(chunks))
    print("Length is : " , len(chunks))
    for index , chunk in enumerate(chunks):
        chunk.export(str(index)+".wav" , format = "wav")
        print("The Chunk is : " ,chunk)
        with sr.AudioFile(str(index)+".wav" ) as source:
            recorded = recog.record(source)
            try:
                rec_text = recog.recognize_google(recorded)
                text_list = text_list + " " + rec_text.capitalize()
                print(rec_text)
            except:
                print("Error")
    st.markdown(f"<p1> {text_list} </p1>" , unsafe_allow_html=True)
    final_result = st.text_area("" , value=text_list)
    print(text_list)

#Creating a Form
with st.form("f1"):
    final_result = st.text_area("" , value=text_list)
    d_btn = st.form_submit_button("Download")
    eviron = os.environ
    print(eviron.get('USERPROFILE'))

    if d_btn:
        with open("transcript.txt" , "w" , ) as file:

            file.write(final_result)






#f&&a==one1A



