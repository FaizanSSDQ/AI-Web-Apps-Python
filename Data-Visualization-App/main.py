import streamlit as st
import pandas as pd

st.markdown("""
            <h1 style='text-align:center; color:blue;'>
            Data Visualization Appication
            </h1>
            """ , unsafe_allow_html= True)
st.markdown("---" , unsafe_allow_html=True)
file_Names = list()
Ext_ = ["xlsx" , "csv"]
rec_file = st.file_uploader("Upload Multiple Files" , type= Ext_ , accept_multiple_files=True)
if rec_file:
    for file in rec_file:
        file_Names.append(file.name)
    selected_files = st.multiselect("Select Multi-files" , options= file_Names)
    if selected_files:
        opt_radio = st.radio("Select Entity against Data" , options=["None" , "Age" , "Fare" , "Pclass"])
        if opt_radio != "None":
            for file in rec_file:
                if file.name in selected_files:
                    shop_data = pd.read_csv(file ) #index_col = 0
                    print("-----/*/*/*/*/*/*/*/*/*/*/*/*/*/")
                    print(list(shop_data[opt_radio]))

            #print(opt_radio)
    #print(" File Names : " , file_Names)

