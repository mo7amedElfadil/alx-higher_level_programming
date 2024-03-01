#!/usr/bin/python3
"""Module send a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter."""
import requests
from sys import argv


def main(letter):
    """Function that sends a POST request with a letter as a parameter."""
    url = "http://0.0.0.0:5000/search_user"
    data = {'q': letter}
    try:
        with requests.post(url, data=data) as response:
            if response.json():
                print("[{}] {}".format(response.json().get('id'),
                                       response.json().get('name')))
            else:
                print("No result")
    except ValueError:
        print("Not a valid JSON")


if __name__ == "__main__":
    if len(argv) < 2:
        main("")
    else:
        main(argv[1])
