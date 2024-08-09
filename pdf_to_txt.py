import os
import fitz
import preprocess_text as pre

def open_file(pdf_path):
    return fitz.open(pdf_path)
    
def extract_text(file):
    text = ""
    for page in file:
        text += page.get_text()
    return text

def save_to_txt(text, pdf_path):
    txt_path = pdf_path.replace('.pdf', '_p2t.txt')
    txt_path = txt_path.replace('resumes', 'extracted_txt')
    
    with open(txt_path, 'w', encoding='utf-8') as file:
        file.write(text)
    
    return txt_path

def convert(pdf_path):
    file = open_file(pdf_path)
    text = extract_text(file)
    
    text = pre.handle_caps(text)
    text = pre.merge_lines(text)

    # return text
    return save_to_txt(text, pdf_path)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("pdf_path")
    args = parser.parse_args()

    if os.path.isfile(args.pdf_path) and args.pdf_path.endswith('.pdf'):
        convert(args.pdf_path)
    else:
        print("pdf path is invalid")
