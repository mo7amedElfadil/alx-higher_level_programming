#!/usr/bin/python3
"""Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id"""
import requests
from sys import argv
from requests.auth import HTTPBasicAuth


def main(username, password):
    """Main function"""
    url = 'https://api.github.com/user'
    response = requests.get(url, auth=HTTPBasicAuth(username, password))
    print(response.json().get('id'))


if __name__ == '__main__':
    main(argv[1], argv[2])
