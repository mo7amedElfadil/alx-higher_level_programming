#!/usr/bin/python3
"""list 10 commits (from the most recent to oldest)
of the repository “rails” by the user “rails”
"""
from sys import argv
import requests


def main(repo, user):
    """
    main function
    """
    url = f"https://api.github.com/repos/{user}/{repo}/commits"
    params = {"per_page": 10}
    with requests.get(url, params=params) as response:
        if response.status_code == 200:
            for commit in response.json():
                sha = commit.get('sha')
                author = commit.get('commit').get('author').get('name')
                print(f"{sha}: {author}")


if __name__ == "__main__":
    main(argv[1], argv[2])
