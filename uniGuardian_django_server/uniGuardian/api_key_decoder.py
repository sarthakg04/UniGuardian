import cryptocode


def decode_openai_api_key(encoded):
    return cryptocode.decrypt(encoded, "openaiapi")
    