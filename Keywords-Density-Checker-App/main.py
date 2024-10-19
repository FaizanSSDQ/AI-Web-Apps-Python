import streamlit as st
import re
st.markdown("""<h1 style = 'text-align : center; color: blue'>
                 Density Checker
            </h1>
            """ , unsafe_allow_html=True)
st.markdown("---" , unsafe_allow_html=True)

text = st.text_area("Enter The Paragraph" , height=200)
col1 , col2 , col3 = st.columns(3 )
word_dict =  dict()

if text:
    col1.markdown(f"<h3>Keywords</h3" , unsafe_allow_html=True)
    col2.markdown(f"<h3>Occurance</h3" , unsafe_allow_html=True)
    col3.markdown(f"<h3>Percentage</h3" , unsafe_allow_html=True)
    sim_text = re.sub("[.?!&';:]" , "" , text)
    words = sim_text.lower().split(" ")
    t_len = len(words)
    #print(words)
    for word in words:
        if word in word_dict:
            word_dict[word]=word_dict[word]+1
        else:
            word_dict[word]=1
    print(word_dict)
    keys = list(word_dict.keys())
    values = list(word_dict.values())
    for i in range(len(keys)):
        col1.markdown(f"<h5>{keys[i]}</h5>" , unsafe_allow_html=True)
        col2.markdown(f"<h5>{values[i]}</h5" , unsafe_allow_html=True)
        col3.markdown(f"<h5>{(values[i]/t_len)*100} % </h5>" , unsafe_allow_html=True)
#for i in words:
 #   st.write(f"<span style='display:inline-block; margin-right:10px;'>`{i}`</span>" , unsafe_allow_html=True)
