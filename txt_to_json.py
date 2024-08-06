import argparse
import os
import logic
import json

def extract_text(txt_path):
    with open(txt_path, 'r', encoding='utf-8') as file:
        return file.read()

# if text wasn't saved to txt file
def convert(text, file_path):
    parsed_data = logic.parse_resume(text)

    json_path = file_path.replace('.pdf', '.json')
    json_path = json_path.replace('.docx', '.json')
    json_path = json_path.replace('resumes', 'parsed_data')

    with open(json_path, 'w') as json_file:
        json.dump(parsed_data, json_file, indent=4)

# if text was saved to txt file
def convert(txt_path):
    text = extract_text(txt_path)

    parsed_data = logic.parse_resume(text)

    json_path = txt_path.replace('_p2t.txt', '_t2j.json')
    json_path = json_path.replace('_d2t.txt', '_t2j.json')
    json_path = json_path.replace('extracted_txt', 'parsed_data')

    with open(json_path, 'w') as json_file:
        json.dump(parsed_data, json_file, indent=4)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("txt_path")
    args = parser.parse_args()

    if os.path.isfile(args.txt_path) and args.txt_path.endswith('.txt'):
        convert(args.txt_path)
    else:
        print("txt path is invalid")
        exit()
    