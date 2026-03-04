import base64
import json


def encrypt(data_dict):

    json_data = json.dumps(data_dict)

    encoded = base64.b64encode(json_data.encode()).decode()

    return encoded


def decrypt(encoded_string):

    decoded = base64.b64decode(encoded_string).decode()

    return json.loads(decoded)
