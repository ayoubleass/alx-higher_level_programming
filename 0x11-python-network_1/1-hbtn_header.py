#!/usr/bin/python3

import urllib.request
import sys

if __name__ == "__main__":
    with urllib.request.urlopen("{}".format(sys.argv[1])) as response:
        headers = dict(response.headers)
        print(headers.get("X-Request-Id"))
