## About
### How to run
###### Install packages
`pip install -r requirements.txt`
###### Install SpaCy package
`python -m spacy download en_core_web_lg`
###### Create folders
1. extracted_txt - this is where the converted resumes will go.
2. parsed_data - this is where the person's details will go.
###### Place resumes in resumes folder
You can delete the sample resumes if you want.
###### Run the following command in a terminal
`python MAIN.py resumes\[my_file.pdf]`
### Notes
I split the process of converting of pdf/docx file to text to json file to make debugging easier. If you want to skip the middle step, do the following: 
1. In app.py: comment line 14 and un-comment line 13.
2. In pdf_to_txt.py: comment line 31 and un-comment line 30.
3. In docx_to_txt.py: comment line 31 and un-comment line 30.
This will remove the text from being saved in the extracted_txt folder.
