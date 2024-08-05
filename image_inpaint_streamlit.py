import streamlit as st
import pathlib
from streamlit_drawable_canvas import st_canvas
import cv2
import numpy as np
import io
import base64
from PIL import Image
import os

# Use /tmp directory for temporary files
DOWNLOADS_PATH = pathlib.Path('/tmp/downloads')
if not DOWNLOADS_PATH.is_dir():
    DOWNLOADS_PATH.mkdir()

def get_image_download_link(img, filename, text):
    """Generates a link to download a particular image file."""
    buffered = io.BytesIO()
    img.save(buffered, format='JPEG')
    img_str = base64.b64encode(buffered.getvalue()).decode()
    href = f'<a href="data:file/txt;base64,{img_str}" download="{filename}">{text}</a>'
    return href

# Set title.
st.sidebar.title('Old Image Restorer')

# Specify canvas parameters in application
uploaded_file = st.sidebar.file_uploader("Upload Image to restore:", type=["png", "jpg"])
image = None
res = None

if uploaded_file is not None:
    # Convert the file to an opencv image.
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, 1)

    stroke_width = st.sidebar.slider("Stroke width: ", 1, 25, 5)
    h, w = image.shape[:2]
    if w > 800:
        h_, w_ = int(h * 800 / w), 800
    else:
        h_, w_ = h, w

    # Create a canvas component.
    canvas_result = st_canvas(
        fill_color='white',
        stroke_width=stroke_width,
        stroke_color='black',
        background_image=Image.open(uploaded_file).resize((h_, w_)),
        update_streamlit=True,
        height=h_,
        width=w_,
        drawing_mode='freedraw',
        key="canvas",
    )
    stroke = canvas_result.image_data

    if stroke is not None:
        if st.sidebar.checkbox('show mask'):
            st.image(stroke)

        mask = cv2.split(stroke)[3]
        mask = np.uint8(mask)
        mask = cv2.resize(mask, (w, h))

    st.sidebar.caption('Happy with the selection?')
    option = st.sidebar.selectbox('Mode', ['None', 'Telea', 'NS', 'Compare both'])

    if option == 'Telea':
        st.subheader('Result of Telea')
        res = cv2.inpaint(src=image, inpaintMask=mask, inpaintRadius=3, flags=cv2.INPAINT_TELEA)[:,:,::-1]
        st.image(res)
    elif option == 'Compare both':
        col1, col2 = st.columns(2)
        res1 = cv2.inpaint(src=image, inpaintMask=mask, inpaintRadius=3, flags=cv2.INPAINT_TELEA)[:,:,::-1]
        res2 = cv2.inpaint(src=image, inpaintMask=mask, inpaintRadius=3, flags=cv2.INPAINT_NS)[:,:,::-1]
        with col1:
            st.subheader('Result of Telea')
            st.image(res1)
        with col2:
            st.subheader('Result of NS')
            st.image(res2)
        if res1 is not None:
            # Display link.
            result1 = Image.fromarray(res1)
            st.sidebar.markdown(
                get_image_download_link(result1, 'telea.png', 'Download Output of Telea'),
                unsafe_allow_html=True)
        if res2 is not None:
            # Display link.
            result2 = Image.fromarray(res2)
            st.sidebar.markdown(
                get_image_download_link(result2, 'ns.png', 'Download Output of NS'),
                unsafe_allow_html=True)

    elif option == 'NS':
        st.subheader('Result of NS')
        res = cv2.inpaint(src=image, inpaintMask=mask, inpaintRadius=3, flags=cv2.INPAINT_NS)[:,:,::-1]
        st.image(res)
    else:
        pass

    if res is not None:
        # Display link.
        result = Image.fromarray(res)
        st.sidebar.markdown(
            get_image_download_link(result, 'output.png', 'Download Output'),
            unsafe_allow_html=True)
