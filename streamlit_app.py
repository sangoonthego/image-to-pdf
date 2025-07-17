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

st.title("Convert Image to PDF File")

uploaded_files = st.file_uploader("Upload Image (Multiselect Available)", type=["png", "jpeg", "jpg"], accept_multiple_files=True)

if uploaded_files:
    st.write(f"Uploaded {len(uploaded_files)} images")
    images = []

    st.header("Options")
    mode = st.selectbox("Resize Mode", ["original", "percent", "pixel"])
    percent, width, height = None, None, None

    if mode == "percent":
        percent = st.slider("Resize percent", 10, 200, 100)
    elif mode == "pixel":
        width = st.number_input("Width", 100, 3000, 800)
        height = st.number_input("Height", 100, 3000, 600)

    watermark_box = st.checkbox("Press to Add Watermark")
    watermark_text = ""
    if watermark_box:
        watermark_text = st.text_input("Add watermark", value="")
        opacity = st.slider("Opacity", 50, 255, 128)
        font_size = st.number_input("Font Size", min_value=0, value=0)
        font_color = st.color_picker("Font Color", "#FFFFFF")
        pos_x = st.number_input("Position X", value=20)
        pos_y = st.number_input("Position Y", value=20)
        position = (pos_x, pos_y)
    else:
        opacity = 0
        font_size = 0
        font_color = "#FFFFFF"
        position = (0, 0)

    st.header("Preview")
    for i, uploaded_file in enumerate(uploaded_files):
        image = Image.open(uploaded_file).convert("RGB")
        image = resize_images(image, mode, percent, width, height)

        if watermark_box and watermark_text.strip():
            image = add_watermark(
                image,
                text=watermark_text,
                position=position,
                opacity=opacity,
                font_size=font_size if font_size > 0 else None,
                font_color=tuple(int(font_color.lstrip("#")[i:i+2], 16) for i in (0, 2, 4))
            )
        images.append(image)
        st.image(image, caption=f"{uploaded_file.name}", use_container_width=True)

    st.header("Export PDF")
    if st.button("Convert to PDF"):
        try:
            pdf_file = pdf_convert(images)
            st.success("Converted Successfully")
            st.download_button(
                label="Download PDF File",
                data=pdf_file,
                file_name="",
                mime="application/pdf"
            )
        except Exception as e:
            st.warning(f"Failed to convert: {e}")
