# pip install tika editdistancehttps://sapling.ai/api_settings#key_config
import requests
from pprint import pprint

def detect_ai_content(api_key, texts):
    response = requests.post(
            "https://api.sapling.ai/api/v1/aidetect",
            json={
                "key": api_key,
                "text": texts
            }
        )
    pprint(response.json()['score'])
    return response.json()['score']
    