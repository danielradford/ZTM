

# Pwned Passwords is a free online repo which stores passwords leaked in data breaches. 
# This script safely checks your passwords on your local machine by making a call to the Pwned Passwords API. 
# This is achieved by sending an encrypted section of the password to the API, the encrypted is done via the SHA1 cryptographic hash function. 
# The API returns a list of hacked passwords which match the section sent to the API. 
# Your full password is checked against this list locally so your full password information never leaves your machine.





import requests
import hashlib
import sys


def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/'+ query_char
    res = requests.get(url)
    if res.status_code !=200:
        raise RuntimeError(f'Error fetching:{res.status_code}, check the api')
    return res

def get_password_leaks_count(hashes,hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0


def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    return get_password_leaks_count(response,tail)

    
def main(*args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f'{password} found {count} times. You should change this password!')
        else:
            print('password is safe!')


if __name__ == '__main__':
    sys.exit(main(*sys.argv[1:]))
    
    
