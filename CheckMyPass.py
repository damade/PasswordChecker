import requests
import hashlib
import sys

def request_api_data(query_key):
    url = 'https://api.pwnedpasswords.com/range/' + query_key
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f"Error fetching: {res.status_code}, check the api and try again")
    return res


def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(":") for line in hashes.text.splitlines())
    for hashed, count in hashes:
        if hashed == hash_to_check:
            return count
    return 0


def pwned_api_check(whatever):
    password = str(whatever)
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    firstFiveHashesChar, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(firstFiveHashesChar)
    return get_password_leaks_count(response,tail)

def main():
    totalPassword = list(map(str, input("What is/are your input(s): ").rstrip().split(",")))
    for password in totalPassword:
        count = pwned_api_check(password)
        if count:
            print(f"{password} was found {count} times.....\noops, You would need to change your password to secure it\n")
        else:
            print(f"{password} was not found.....\nYour password is secure, Carry on !!!!\n")
    return 'done!'

if __name__ ==  "__main__":
    sys.exit(main())