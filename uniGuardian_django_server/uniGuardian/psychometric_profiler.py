import os
import requests
import json
import pprint

def create_user_profile(API_KEY, user_id, file_path):
    headers = {}
    payload = {}
    files = load_file(file_path)
    BASE_URL = "https://api.humantic.ai/v1/user-profile/create"  # Base URL for the CREATE endpoint
    url = f"{BASE_URL}?apikey={API_KEY}&userid={user_id}"
    response = requests.request("POST", url, data=payload, headers=headers, files=files)
    #print(response.status_code, response.text)
    return response.status_code, response.text

def modify_user_persona(API_KEY, user_id, PERSONA):
    BASE_URL = "https://api.humantic.ai/v1/user-profile"  # Base URL for the FETCH endpoint
    headers = {
        'Content-Type': 'application/json'
    }
    url = f"{BASE_URL}?apikey={API_KEY}&id={user_id}&persona={PERSONA}"
    response = requests.request("GET", url, headers=headers)
    print(response.status_code, response.text)
    return response.status_code, response.text

def load_file(file_path):
    try:
        files = [
          ("document", ("SOP.pdf", open(file_path, "rb"), "application/octet-stream"))
        ]
    except FileNotFoundError as e:
        returnLog = "Your document is not found. Please enter the correct file path."
        print(f"Your document is not found. Please enter the correct file path.\n"
          f"{e}")
    return files

def convert_to_json_file(text, user_id, output_dir):
    json_data = json.loads(text)
    output_file = output_dir + "PsyProfile_" + user_id + ".json"
    try:
        with open(output_file, "w", encoding='utf-8') as of:
            json.dump(json_data, of, ensure_ascii = False, indent = 4)
    except FileNotFoundError as e:
        returnLog = "The output directory cannot be found. Please enter the correct path."
        print(f"The output directory cannot be found. Please enter the correct path.\n"
          f"{e}")
    return output_file

def check_json_file(output_file):
    f = open(output_file)
    data = json.load(f)
    if(len(data["results"]["personality_analysis"]) == 0):
        warningLog = "No analysis result is returned. Please check the content of your document."
        print(warningLog)
    return data

def profile_psychometric(file_path, user_id, output_dir, API_KEY, PERSONA):
    create_user_profile(API_KEY, user_id, file_path)
    statu_code, ret_text = modify_user_persona(API_KEY, user_id, PERSONA)
    output_file = convert_to_json_file(ret_text, user_id, output_dir)
    check_json_file(output_file)
    return output_file

# user_id = "jiaqili"
# file_path = "./Materials/SOP.pdf"
# output_dir = "./Materials/"
# API_KEY = "chrexec_96effa3d5b5f3c0de52193e04e91e087"
# PERSONA = "hiring"
# profile_psychometric(file_path, user_id, output_dir, API_KEY, PERSONA)