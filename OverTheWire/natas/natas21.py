import base64
import requests
from requests.auth import HTTPBasicAuth

basic_auth = HTTPBasicAuth('natas20', 'p5mCvP7GS2K6Bmt3gqhM2Fc1A5T8MVyw')

url = "http://natas20.natas.labs.overthewire.org/index.php?debug"


def encode_cookie(cookie: str) -> str:
    encoded_cookie = base64.b16encode(cookie.encode('ascii')).lower()
    return encoded_cookie.decode('ascii')


def send_request() -> str:
    cookie = "PHPSESSID=" + "brafbmkkbb2tmhhrn5m68r36n2"
    headers = {'Content-Type': 'text/html; charset=UTF-8',
               'Cookie': cookie}
    body = {"name": "admin"}
    response = requests.post(url, headers=headers,
                             auth=basic_auth, json=body, verify=False)
    return response.text


if __name__ == '__main__':
    text = send_request()
    print(text)
