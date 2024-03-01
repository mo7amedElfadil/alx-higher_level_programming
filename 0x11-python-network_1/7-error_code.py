#!/usr/bin/python3
"""takes in a URL, sends a request to the URL and
displays the body of the response (decoded in utf-8)
"""
import requests
from sys import argv


def main(url):
    """main function to send request
    """
    with requests.get(url) as response:
        if response.status_code >= 400:
            print("Error code: {}".format(response.status_code))
        else:
            print(response.text)


if __name__ == "__main__":
    main(argv[1])
