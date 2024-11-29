import requests
import urllib
import string

from utils import utils


basic_auth = ('natas28', '1JNwQM1Oi6J6j1k49Xyw7ZN6pXMQInVj')

url = "http://natas28.natas.labs.overthewire.org/index.php"
headers = {"Content-Type": "application/x-www-form-urlencoded"}

letters = string.ascii_letters

def send_request(session, query) -> str:
    body = {"query": query}
    response = session.post(url,
                    headers=headers,
                    data=body)
    result = response.url.split("=")[1]
    return urllib.parse.unquote(result)

if __name__ == '__main__':
    letter_to_responses = {}
    session = requests.Session()
    session.auth = basic_auth
    query = ""
    for letter in letters:
        query = "Z" * 9 + letter
        letter_to_responses[query] = send_request(session, query)
    responses = list(letter_to_responses.values())
    prefix = utils.common_prefix_list(responses)
    suffix = utils.common_suffix_list(responses)
    print(f"Common prefix: {prefix}")
    print(f"Common suffix: {suffix}")
    different_parts = {k: s[len(prefix):len(s) - len(suffix)] for k, s in letter_to_responses.items()}
    for k, s in different_parts.items():
        print(f"{s}")