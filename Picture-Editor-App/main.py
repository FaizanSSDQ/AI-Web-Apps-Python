import streamlit as st
from PIL import Image
from PIL import ImageFilter
st.markdown("""
            <h1 style='text-align: center';>
            Image Editor
            </h1>
            """ ,   unsafe_allow_html=True)
st.markdown("---")
formats = ["jpg" , "png" , "jpeg"]
rec_image = st.file_uploader("Upload Your Image" , type=formats)
size = st.empty()
mode = st.empty()
format_ = st.empty() 
info = st.empty()
if rec_image:
    info.markdown("""
            <h2 style='text-align: center';>
            Information
            </h2>
            """ ,   unsafe_allow_html=True)
    st.image(rec_image)
    Op_image = Image.open(rec_image)
    print(Op_image.mode)
    mode.markdown(f"###### Mode :  {Op_image.mode}")
    print(Op_image.format)
    format_.markdown(f"###### Format :  {Op_image.format}")
    print(Op_image.size)
    size.markdown(f"###### Size :  {Op_image.size}")
    st.markdown("""
            <h4 style='text-align: center';>
            Resizing
            </h4>
            """ ,   unsafe_allow_html=True)
    width =st.number_input("Enter The Width " , value=Op_image.width)
    height =st.number_input("Enter The Height " , value=Op_image.height)


    st.markdown("""
            <h4 style='text-align: center';>
            Rotation With Angle
            </h4>
            """ ,   unsafe_allow_html=True)
    degrees =st.number_input("Enter The Degree of Rotation ")
    #rot_img = Op_image.rotate(degrees)
    #st.image(rot_img)



    st.markdown("""
            <h4 style='text-align: center';>
            Filters
            </h4>
            """ ,   unsafe_allow_html=True)
    filters_set = ["None" , "Blur" , "Detail" , "Emboss" , "Smooth" , "Greyscale"]
    filters_values =st.selectbox("Filters"  , options= filters_set)
    s_btn = st.button("Submit")
    if s_btn:
        edited = Op_image.resize((width , height)).rotate(degrees)
        filtered = edited
        if filters_values != "None":
            if filters_values == "Blur":
                filtered = edited.filter(ImageFilter.BLUR)
            elif filters_values == "Detail":
                filtered = edited.filter(ImageFilter.DETAIL)
            elif filters_values == "Embos":
                filtered = edited.filter(ImageFilter.EMBOSS)
            elif filters_values == "Smooth":
                filtered = edited.filter(ImageFilter.CONTOUR)
            elif filters_values == "Greyscale":
                filtered = edited.convert("L")
            else:
                st.write("Thats It")
            
                
        st.image(filtered)

