import streamlit as st
from PIL import Image
from imagenet import img_class



uploaded_file=st.file_uploader('Загрузи сюда любую картинку',type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)
    
    if st.button('Это что'):
        #st.write(image)
        st.success(img_class(image))