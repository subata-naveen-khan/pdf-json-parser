import fitz  # PyMuPDF
import spacy
import re
import json
import os
# from spacy.matcher import Matcher

nlp = spacy.load("en_core_web_md")

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def parse_resume(text):
    doc = nlp(text)

    parsed_data = {
        "name": "",
        "email": "",
        "phone": "",
        "education": [],
        "experience": [],
        "skills": []
    }
       
    # name
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            parsed_data["name"] = ent.text
            break
    
    # email
    email = re.findall(r'\S+@\S+', text)
    if email:
        parsed_data["email"] = email[0]
    
    # phone number // not complete
    phone = re.findall(r'\b\d{10}\b', text)
    if phone:
        parsed_data["phone"] = phone[0]
    
    # TODO: extract education, experience, and skills

    return parsed_data

def process_resume(pdf_path):
    text = extract_text_from_pdf(pdf_path)
    parsed_data = parse_resume(text)
    json_path = pdf_path.replace('.pdf', '_md.json')
    json_path = json_path.replace('resumes', 'parsed_data')
    with open(json_path, 'w') as json_file:
        json.dump(parsed_data, json_file, indent=4)
    print(f"Processed {pdf_path} and saved as {json_path}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("pdf_path")
    args = parser.parse_args()

    if os.path.isfile(args.pdf_path) and args.pdf_path.endswith('.pdf'):
        process_resume(args.pdf_path)
    else:
        print("pdf path is invalid")
