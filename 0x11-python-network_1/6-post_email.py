#!/usr/bin/python3
"""Send a POST request to the passed URL with the email as a parameter."""
import requests
from sys import argv


def main(url, email):
    """Send a POST request to the passed URL with the email
    as a parameter."""
    with requests.post(url, data={'email': email}) as response:
        print(response.text)


if __name__ == "__main__":
    if len(argv) > 2:
        main(argv[1], argv[2])
