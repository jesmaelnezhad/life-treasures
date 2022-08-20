import hashlib
import base64
import json
import requests


def GetAuthenticatedWithHMAC():
    hmac_key = "keykeykeykeykeykey"
    body_str = ""
    body_b64 = base64.b64encode(bytes(body_str, "utf-8"))
    body_b64_encoded = base64.b64decode(body_b64).decode("utf-8", "ignore")
    request_path = "/api/users/verify"
    request_method = "GET"
    public_key = "PUBLIC_KEY"

    phrase = "{}.{}.{}.{}.{}".format(body_b64_encoded, request_path, request_method, hmac_key, public_key)

    phrase_hmac_encoding = hashlib.sha256(phrase.encode('utf-8')).hexdigest()


    url = "https://api.example.com{}".format(request_path)

    headers = {
        "key" : phrase_hmac_encoding
    }

    response = requests.get(url, headers=headers, data=body_str)
    print(response.text)

GetAuthenticatedWithHMAC()
