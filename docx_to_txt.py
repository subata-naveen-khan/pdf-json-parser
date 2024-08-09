import os
import docx
import preprocess_text as pre

def open_file(docx_path):
    return docx.Document(docx_path)
    
def extract_text(file):
    text = []
    for paragraph in file.paragraphs:
        text.append(paragraph.text)  
    return '\n'.join(text)

def save_to_txt(text, docx_path):
    txt_path = docx_path.replace('.docx', '_d2t.txt')
    txt_path = txt_path.replace('a_res', 'extracted_txt')
    
    with open(txt_path, 'w', encoding='utf-8') as file:
        file.write(text)
    
    return txt_path

def convert(docx_path):
    file = open_file(docx_path)
    text = extract_text(file)
    
    text = pre.handle_caps(text)
    text = pre.merge_lines(text)

    # return text
    return save_to_txt(text, docx_path)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("docx_path")
    args = parser.parse_args()

    if os.path.isfile(args.docx_path) and args.docx_path.endswith('.docx'):
        convert(args.docx_path)
    else:
        print("docx path is invalid")
