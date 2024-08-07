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
    pattern = r"(?:\(?\+?0{0,2}\d{1,3}\)?[-.\s]?)?(\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4})"
    
    matches = re.findall(pattern, text)
    for match in matches:
        phone.append(match.strip())

    return phone

def get_education(text):
    education = []

    # pattern = r"(?i)(?:\bBs|\bB\.\w+|\bM\.\w+|\bPh\.D\.\w+|\bBachelor(?:'s)?|\bMaster(?:'s)?|\bPh\.?D|\bMatric(?:\s|ulation)|\bIntermediate|\bO-Level(?:s)?|\bA-Level(?:s)?)\s*(?::\s*)?(?:\w+\s)*\w+"
    pattern = re.compile(r"\b(?:Bachelor(?:'s)?|B.Tech|B\.?A\.?|B\.?S\.?|B\.?Eng|Master(?:'?s)?|M\.?A\.?|M\.?S\.?|M\.?Eng|Doctor(?:ate|al)?|Ph\.?D\.?|D\.?Sc\.?|Graduate|Postgraduate|Undergraduate)\b")

    for line in text.splitlines():
        if pattern.search(line):
            education.append(line.strip())

    # matches = re.findall(pattern, text)
    # for match in matches:
    #     education.append(match.strip())
        
    return education

def parse_resume(text):
    nlp = spacy.load("en_core_web_md")

    doc = nlp(text)

    parsed_data = { "name": "", "email": "", "phone": "", "education": [], "experience": [], "skills": [] }
    
    parsed_data["email"] = get_email(text)
    parsed_data["name"] = get_name(doc)
    parsed_data["phone"] = get_phone_number(text)
    # parse_resume["skills"] = get_skills(text)
    parsed_data["education"] = get_education(text)

    return parsed_data
