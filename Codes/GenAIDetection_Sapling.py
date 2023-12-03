# pip install tika editdistancehttps://sapling.ai/api_settings#key_config
import requests
from pprint import pprint
import textract
import re
from tika import parser # pip install tika
from nltk import tokenize
from PyPDF2 import PdfReader 

def load_content(file_path):
    try:
        reader = PdfReader(file_path)
    except FileNotFoundError as e:
        print(f"Your resume is not found. Please enter the correct file path.\n"
          f"{e}")
    #page = reader.pages[0] 

    resume_text = ""
    for page in reader.pages:
        resume_text += page.extract_text() 
    print(resume_text)
    return resume_text


    # try:
    #     text = textract.process(file_path, method='pdfminer')
    #     print(text)
    # except FileNotFoundError as e:
    #     print(f"The file is not found. Please enter the correct file path.\n"
    #       f"{e}")

    #text = parser.from_file(file_path)
    #print(str(text['content']))

    #extracted_strings = re.findall(r'"(.*?)"', str(text['content']))
    #extracted_strings = tokenize.sent_tokenize(str(text['content']))
    # extracted_strings = tokenize.sent_tokenize(resume_text)
    # #extracted_strings = re.split(r' *[\.\?!][\'"\)\]]* *', str(text['content']))
    # print(extracted_strings)
    # return extracted_strings

def detect_gen_ai(api_key, texts):
    response = requests.post(
            "https://api.sapling.ai/api/v1/aidetect",
            json={
                "key": api_key,
                "text": texts
            }
        )
    pprint(response.json())
    
    # for text in texts:
    #     response = requests.post(
    #         "https://api.sapling.ai/api/v1/aidetect",
    #         json={
    #             "key": api_key,
    #             "text": text
    #         }
    #     )
    #     pprint(response.json())


api_key = "PX41HQGZ4FAV34HWVO3BQAOGULQH91AQ"
texts = load_content("./Materials/Sarthak SOP.pdf")
detect_gen_ai(api_key, texts)
