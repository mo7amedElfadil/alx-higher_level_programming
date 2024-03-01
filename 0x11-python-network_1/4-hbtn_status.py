#!/usr/bin/python3
""" fetch https://alx-intranet.hbtn.io/status
"""
import requests


def my_fetch(link):
    """ function to fetch from a link
    """
    with requests.get(link) as response:
        html = response.content.decode("utf-8")

        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))


if __name__ == "__main__":
    my_fetch("https://alx-intranet.hbtn.io/status")
