import streamlit as st
from PIL import Image
import pytesseract
from shutil import which

tesseract_path = which("tesseract")
st.write("Tesseract path:", tesseract_path)
pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

def load_image(image_file):
    return Image.open(image_file)

def main():
    st.title("OCR with Tesseract")
    image_file = st.file_uploader("Upload Image", type=['png', 'jpeg', 'jpg'])

    if image_file is not None:
        image = load_image(image_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)
        if st.button("Recognize Text"):
            result_text = pytesseract.image_to_string(image)
            st.write(result_text)

if __name__ == "__main__":
    main()
