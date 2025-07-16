import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from PIL import Image
import io

from utils.order import reorder_images
from utils.watermark import add_watermark
from utils.resize import resize_images
from utils.pdf import pdf_convert

st.title("📸 Convert Image to PDF File")

uploaded_files = st.file_uploader("Upload Image (Multiselect Available)", type=["png", "jpeg", "jpg"], accept_multiple_files=True)

if uploaded_files:
    st.write(f"Uploaded {len(uploaded_files)} images")
    images = []

    st.header("Options")
    mode = st.selectbox("Resize Mode", ["Original", "Percent", "Pixel"])
    percent, width, height = None, None, None
    if mode == "percent":
        percent = st.slider("Resize percent", 10, 200, 100)
    elif mode == "pixel":
        width = st.number_input("Width", 100, 3000, 800)
        height = st.number_input("Height", 100, 3000, 600)

    watermark_box = st.checkbox("Press to Add Watermark")
    watermark_text = "" 
    if watermark_box:
        watermark_text = st.text_input("Add watermark", value="Add watermark")

    st.header("Preview")
    for idx, uploaded_file in enumerate(uploaded_files):
        image = Image.open(uploaded_file).convert("RGB")
        image = resize_images(image, mode, percent, width, height)
        if watermark_box and watermark_text:
            image = add_watermark(image, watermark_text, position=(20, 20))
        images.append(image)
        st.image(image, caption=uploaded_file.name, use_container_width=True)

    st.header("Export PDF")
    if st.button("Convert to PDF"):
        try:
            pdf_data = pdf_convert(images)
            st.success("Converted Successfully")
            st.download_button(
                label="Download PDF File",
                data=pdf_data,
                file_name="",
                mime="application/pdf"
            )
        except Exception as e:
            st.warning(f"Failed to convert: {e}")
