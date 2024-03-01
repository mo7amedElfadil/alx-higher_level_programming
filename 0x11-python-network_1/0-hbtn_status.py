#!/usr/bin/python3
""" fetch https://alx-intranet.hbtn.io/status
"""
import urllib.request


def my_fetch(link):
    """ function to fetch from a link
    """
    with urllib.request.urlopen(link) as response:
        html = response.read()

        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(html.decode("utf-8")))


if __name__ == "__main__":
    my_fetch("https://alx-intranet.hbtn.io/status")
