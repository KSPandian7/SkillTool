import streamlit as st
import pdfplumber
import docx
import pandas as pd
import os

def extract_text_from_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

def extract_text_from_docx(file):
    doc = docx.Document(file)
    return "\n".join([para.text for para in doc.paragraphs])

def extract_text_from_excel(file):
    df = pd.read_excel(file)
    return df.to_string(index=False)

def extract_text_from_csv(file):
    df = pd.read_csv(file)
    return df.to_string(index=False)

def extract_text_from_txt(file):
    return file.read().decode("utf-16")

def main():
    st.title("📄 Universal File Text Extractor")
    st.write("Upload a file (PDF, DOCX, Excel, CSV, TXT) and extract its text content.")

    uploaded_file = st.file_uploader("Choose a file", type=["pdf", "docx", "xlsx", "csv", "txt"])

    if uploaded_file is not None:
        file_type = os.path.splitext(uploaded_file.name)[1].lower()

        if file_type == ".pdf":
            text = extract_text_from_pdf(uploaded_file)
        elif file_type == ".docx":
            text = extract_text_from_docx(uploaded_file)
        elif file_type == ".xlsx":
            text = extract_text_from_excel(uploaded_file)
        elif file_type == ".csv":
            text = extract_text_from_csv(uploaded_file)
        elif file_type == ".txt":
            text = extract_text_from_txt(uploaded_file)
        else:
            text = "Unsupported file type."

        st.subheader("📃 Successfully Extracted Text.")
        st.text_area("Extracted content:", value=text, height=69)

        search = st.text_input("Search within extracted text...")

        if search:
            st.subheader("Search Reasult ↓")
            lines = text.split('\n')
            results = [line for line in lines if search.lower() in line.lower()]
            if results :
                for res in results:
                    st.write(f"→ {res}")
            else:
                st.warning("No matches found.")
    else:
        st.info("👆 Please upload a file to get started.")


if __name__ == "__main__":
    main()
