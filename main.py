import streamlit as st
from PIL import Image, ImageFilter
import io

st.title("Image Detection App")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
# processed_image = None

if uploaded_file is not None:
    # Open the uploaded image
    image = Image.open(uploaded_file)
    

    col1 , col2 = st.columns(2)

    with col1:
    # Display the original image
        st.image(image, caption='Uploaded Image', use_column_width=True)
        st.write("")

    def objects_detection(image):
        # Process the image (example: apply a blur filter)
        processed_image = image.Detection(ImageFilter.BLUR)
        with col2:
            st.image(processed_image, caption='Processed Image', use_column_width=True)

    st.button(
        label="Analyse Image",
        on_click=lambda: objects_detection(image)
    )

    


    # # Process the image (example: apply a blur filter)
    # processed_image = image.filter(ImageFilter.BLUR)
    # st.image(processed_image, caption='Processed Image', use_column_width=True)

    # Provide a download button for the processed image
    # buf = io.BytesIO()
    # processed_image.save(buf, format="PNG")
    # byte_im = buf.getvalue()
    
    # st.download_button(
    #     label="Download Processed Image",
    #     data=byte_im,
    #     file_name="processed_image.png",
    #     mime="image/png"
    # )