#!/usr/bin/python3
"""Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id"""
import requests
from sys import argv


def main(_, token):
    """Main function"""
    url = 'https://api.github.com/user'
    headers = {'Authorization': f'Bearer {token}'}
    with requests.get(url, headers=headers) as response:
        print(response.json().get('id'))


if __name__ == '__main__':
    main(argv[1], argv[2])
