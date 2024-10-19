import streamlit as st
from bs4 import BeautifulSoup
import requests

st.markdown("<h1 style = 'text-align: center; color: red;'> Youtube KeyWords Scrapper</h1>" , unsafe_allow_html=True)
page = requests.get("https://www.youtube.com/watch?v=9qRHmNpRg38")
soup = BeautifulSoup(page.content , 'lxml')
meta_tag = soup.select("meta[name = 'keywords']")
print("Meta Tags are : " , meta_tag)
print("The Status Code is : " , -page.status_code)
print("Separately: " , meta_tag[0]["content"])
print(type(meta_tag))


f1 = st.form("f1")
rec_url = f1.text_input("Enter The URL to Generate Keywords" )
but_state = f1.form_submit_button("Generate Keywords")
if but_state:
    page = requests.get(rec_url)
    soup = BeautifulSoup(page.content , 'lxml')
    meta_tag = soup.select("meta[name = 'keywords']")
    keywords = meta_tag[0]["content"]
    title = soup.find("title")
    print("Meta Tags are : " , meta_tag)    
    print("The Status Code is : " , -page.status_code)
    print("Separately: " , keywords)
    st.markdown("<h2>Title</h2>" , unsafe_allow_html=True)
    st.markdown(f"{title.text}")
    st.markdown("<h2>Tags</h2>" , unsafe_allow_html=True)
    st.text_area("" , value=keywords , height=150  )
    print(type(meta_tag))
    print(page.status_code)