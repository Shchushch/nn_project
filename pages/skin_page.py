import streamlit as st
from PIL import Image
from skin.skin import get_evil



uploaded_file=st.file_uploader('Загрузи сюда картинку новообразования',type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)
    
    if st.button('Это что'):
        st.success(get_evil(image))