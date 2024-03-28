#!/usr/bin/python3
"""
This script takes in a URL,
sends a request to the URL and displays
the value of the X-Request-Id variable found in the header of the response.
"""


if __name__ == "__main__":
    import urllib.request
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        response_body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(response_body)))
        print("\t- content: {}".format(response_body))
        print("\t- utf8 content: {}".format(response_body.decode("utf-8")))
