import spacy
import re

def get_name(doc):
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            return (ent.text).strip()
def get_email(text):
    email = re.findall(r'\S+@\S+', text)
    if email:
        return email[0]

def get_phone_number(text):
    phone = []
    # pattern = r'(?:(?:0092|\+92)[-.\s]?|\d{1})?(\d{3})[-.\s]?(\d{3})[-.\s]?(\d{4})'
    pattern = r"(?:\(?\+?0{0,2}\d{1,3}\)?[-.\s]?)?(\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4})"
    
    matches = re.findall(pattern, text)
    for match in matches:
        phone.append(match.strip())

    return phone
# def get_skills(text):
#     return []

def extract_education_from_resume(text):
    education = []

    pattern = r"(?i)(?:\bBs|\bB\.\w+|\bM\.\w+|\bPh\.D\.\w+|\bBachelor(?:'s)?|\bMaster(?:'s)?|\bPh\.D|\bMatric|\bIntermediate|\bO-Level(?:s)?|\bA-Level(?:s)?)\s*(?::\s*)?(?:\w+\s)*\w+"

    matches = re.findall(pattern, text)
    for match in matches:
        education.append(match.strip())
        
    return education

def parse_resume(text):
    nlp = spacy.load("en_core_web_lg")

    doc = nlp(text)

    parsed_data = {
        "name": "",
        "email": "",
        "phone": "",
        "education": [],
        "experience": [],
        "skills": []
    }
    
    # email
    parsed_data["email"] = get_email(text)
       
    # name
    parsed_data["name"] = get_name(doc)
    
    # phone number 
    parsed_data["phone"] = get_phone_number(text)

    # parse_resume["skills"] = get_skills(text)

    parsed_data["education"] = extract_education_from_resume(text)

    return parsed_data
