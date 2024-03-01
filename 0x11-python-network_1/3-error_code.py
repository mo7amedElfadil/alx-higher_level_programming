#!/usr/bin/python3
"""takes in a URL, sends a request to the URL and
displays the body of the response (decoded in utf-8)
"""
import urllib.request as request
import urllib.error
from sys import argv


def main(url):
    """main function to send request
    """
    try:
        req = request.Request(url)
        with request.urlopen(req) as response:
            print(response.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))


if __name__ == "__main__":
    main(argv[1])
