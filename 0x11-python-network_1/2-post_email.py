#!/usr/bin/python3
"""Send a POST request to the passed URL with the email as a parameter."""
import urllib.request as request
import urllib.parse as parse
from sys import argv


def main(url, email):
    """Send a POST request to the passed URL with the email
    as a parameter."""
    data = parse.urlencode({"email": email}).encode("utf-8")
    req = request.Request(url, data)
    with request.urlopen(req) as response:
        print(response.read().decode("utf-8"))


if __name__ == "__main__":
    if len(argv) > 2:
        main(argv[1], argv[2])
