## About
### How to run
1. **Install packages**

	`pip install -r requirements.txt`
3.  **Install SpaCy package**
	
 	`python -m spacy download en_core_web_lg`
4. **Place resumes in resumes folder**
	
 	You can delete the sample resumes if you want.
5. **Run the program**
	
 	- To process one file in resumes folder:
		`python app.py resumes\[my_file.pdf]`
	- To process all files in resumes folder:
		`python app2.py`
### Notes
I split the process of converting of pdf/docx file to text to json file to make debugging easier. If you want to skip the middle step, do the following: 
1. In app.py: comment line 15 and un-comment line 14, 
   or in app2.py, comment line 16 and un-comment line 15
2. In pdf_to_txt.py: comment line 31 and un-comment line 30.
3. In docx_to_txt.py: comment line 31 and un-comment line 30.

This will prevent the text from being saved in the `extracted_txt` folder. You can delete it if you want.
