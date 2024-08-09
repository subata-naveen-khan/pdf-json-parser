# Run this if you want to process a single file. Enter the file path as an argument in the command line
import os
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
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("file_path")
    args = parser.parse_args()

    if os.path.isfile(args.file_path) and (args.file_path.endswith('.pdf') or args.file_path.endswith('.docx')):
        process_resume(args.file_path)
    else:
        print("pdf path is invalid")
