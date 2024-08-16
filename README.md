## About

### How to run

1. **Install packages**
   `pip install -r requirements.txt`
2. **Install SpaCy package**
   `python -m spacy download en_core_web_lg`
3. **Place resumes in resumes folder**
   You can delete the sample resumes if you want.
4. **Run the program**
   - To process one file in resumes folder:
     `python app.py resumes\[my_file.pdf]`
   - To process all files in resumes folder:
     `python app2.py`

### Notes

I split the process of converting the pdf/docx file to text, and text to json file, in order to make debugging easier. You'll need to create an `extracted_txt` folder in the root directory to save the txt file. If you don't want to save the text, do the following:

1. In app.py: comment line 15 and un-comment line 14,
   or in app2.py, comment line 16 and un-comment line 15
2. In pdf_to_txt.py: comment line 31 and un-comment line 30.
3. In docx_to_txt.py: comment line 31 and un-comment line 30.
   This will remove the need for the `extracted_txt` folder and the text won't be saved.
