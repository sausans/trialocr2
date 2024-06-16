import streamlit as st
from PIL import Image
import pytesseract
from shutil import which
import os

# Attempting to find the real Tesseract executable
tesseract_path = which("tesseract")
if tesseract_path:
    pytesseract.pytesseract.tesseract_cmd = tesseract_path
else:
    st.error("Tesseract not found. Please ensure it's installed and on your PATH.")

def process_image_and_generate_drafts(image):
    try:
        extracted_text = pytesseract.image_to_string(image, lang='eng')
    except Exception as e:
        st.warning(f"pytesseract failed with error: {e}. Using tesserocr instead.")
        extracted_text = tesserocr.image_to_text(image)
        
    context = extracted_text.strip()
    #original_embedding = get_embedding(context)
    #rec_docs = query_pinecone(original_embedding)
    #draft_responses = chain_of_thought_prompting(context, rec_docs)

    return context#, draft_responses

def load_image(image_file):
    return Image.open(image_file)

def main():
    st.title("OCR with Tesseract")
    image_file = st.file_uploader("Upload Image", type=['png', 'jpeg', 'jpg'])

    if image_file is not None:
        image = load_image(image_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)
        if st.button("Recognize Text"):
            result_text = process_image_and_generate_drafts(image)
            st.write(result_text)

if __name__ == "__main__":
    main()
