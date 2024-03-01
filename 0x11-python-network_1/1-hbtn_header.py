#!/usr/bin/python3
""" fetch https://alx-intranet.hbtn.io/status
"""
import urllib.request
from sys import argv


def my_fetch(link):
    """ function to fetch from a link
    """
    with urllib.request.urlopen(link) as response:
        print(response.getheader('X-Request-Id'))


if __name__ == "__main__":
    if len(argv) > 1:
        my_fetch(argv[1])
