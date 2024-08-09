# Run this instead of app.py to process all the files in the resumes folder. No need to enter the file paths
import os
import glob
import pdf_to_txt
import docx_to_txt
import ptxt_to_json

def process_resume(file_path):
    if file_path.endswith('.pdf'):
        txt = pdf_to_txt.convert(file_path)

    elif file_path.endswith('.docx'):
        txt = docx_to_txt.convert(file_path)
    
    # txt_to_json.convert(txt, file_path)
    ptxt_to_json.convert(txt)

if __name__ == "__main__":
    folder_path = 'resumes/'

    for file_name in glob.glob(os.path.join(folder_path, '*')):
        if os.path.isfile(file_name) and (file_name.endswith('.pdf') or file_name.endswith('.docx')):
            process_resume(file_name)
