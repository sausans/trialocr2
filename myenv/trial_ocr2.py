import streamlit as st
from PIL import Image
import pytesseract
from shutil import which
import os
import subprocess

def check_tesseract():
    # Check if Tesseract is in the PATH
    tesseract_path = subprocess.getoutput('which tesseract')
    if tesseract_path:
        return f"Tesseract is installed at: {tesseract_path}"
    else:
        return "Tesseract is not installed."

def list_installed_packages():
    # This will list all installed packages in the environment
    installed_packages = subprocess.getoutput('dpkg -l')
    return installed_packages

def main():
    st.title('Tesseract OCR Checker')
    if st.button('Check Tesseract Installation'):
        result = check_tesseract()
        st.text(result)
    
    if st.button('List Installed Packages'):
        packages = list_installed_packages()
        st.text_area("Installed Packages:", packages, height=300)

if __name__ == '__main__':
    main()