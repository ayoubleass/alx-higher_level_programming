#!/usr/bin/python3
"""This script takes your GitHub credentials (username and password)
and uses the GitHub API to display your id"""


if __name__ == "__main__":
    import sys
    import requests
    url = "https://api.github.com/user"
    headers = {"Authorization": "Bearer " + sys.argv[2]}
    r = requests.get(url, headers=headers)
    print("{}".format(r.json().get('id')))
