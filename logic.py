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

def get_skills(text):
    with open('skills_list.txt', 'r') as file:
    # Read all lines and strip the newline character
        skills_list = [line.strip() for line in file.readlines()]

    skills = []

    for skill in skills_list:
        if skill.lower() in text.lower():
            skills.append(skill)
    
    return skills

# def get_education(text):
#     education = []
#     with open("regex_education.txt", 'r') as file:
#         pattern = file.read()
#     pattern = re.compile(pattern, re.VERBOSE)

#     # for line in text.splitlines():
#     #     if pattern.search(line):
#     #         education.append(line.strip())
    
#     matches = re.findall(pattern, text)
#     for match in matches:
#         education.append(match.strip())
  
#     return education

def parse_resume(text):
    nlp = spacy.load("en_core_web_md")
    doc = nlp(text)

    parsed_data = { "name": "", "email": "", "phone": "", "education": [], "experience": [], "skills": [] }
    
    parsed_data["email"] = get_email(text)
    parsed_data["name"] = get_name(doc)
    parsed_data["phone"] = get_phone_number(text)
    parsed_data["skills"] = get_skills(text)
    # parsed_data["education"] = get_education(text)

    return parsed_data
