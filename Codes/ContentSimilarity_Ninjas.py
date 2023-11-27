import requests
from PyPDF2 import PdfReader 
import textract
from nltk import tokenize
import nltk
nltk.download('punkt')


#API_KEY = 'r3xKWHWe9w9K93aRSlCQQA==PHSbZWRAoVvUdK7h'
def compare_similarity(text1, text2, API_KEY):
    body = { 'text_1': text1, 'text_2': text2 }
    api_url = 'https://api.api-ninjas.com/v1/textsimilarity'
    response = requests.post(api_url, headers={'X-Api-Key': API_KEY}, json=body)
    if response.status_code == requests.codes.ok:
        print(response.text)
        return response.text
    else:
        print("Error:", response.status_code, response.text)
        return "Error:" + response.status_code + response.text

def parse_sop(file_path):
    try:
        text = textract.process(file_path, method='pdfminer')
    except FileNotFoundError as e:
        print(f"The sop is not found. Please enter the correct file path.\n"
          f"{e}")
    #print(text)
    sentences = tokenize.sent_tokenize(str(text))
    print(sentences)
    #return sentences

def parse_rl(file_path):
    try:
        text = textract.process(file_path, method='pdfminer')
    except FileNotFoundError as e:
        print(f"The letter of recommendation is not found. Please enter the correct file path.\n"
          f"{e}")
    print(text)
    return text


    

parse_sop("./Materials/SOP.pdf")

    

