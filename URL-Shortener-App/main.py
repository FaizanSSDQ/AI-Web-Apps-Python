import streamlit as st
import pyshorteners as pyst
import pyperclip

My_short =  pyst.Shortener()
st.markdown("<h1 style = 'text-align: center;'> URL Shortener App </h1>" , unsafe_allow_html=True)


def copying():
    pyperclip.copy(short_url)


f1 = st.form(key="f1")
f1.empty()
rec_url = f1.text_input("Please Enter URL: ")
form_state = f1.form_submit_button("Short")
if form_state:
    f1.markdown(f"Actual URL is : `{rec_url}`")
    short_url = My_short.tinyurl.short(rec_url)
    f1.markdown(f"Shortened URL is : `{short_url}`")
    st.title("Shorted URL")
    st.markdown(f"<h6 style='text-align:center;'>{short_url}</h6>" , unsafe_allow_html=True)
    st.button("Copy"  , on_click=copying)




