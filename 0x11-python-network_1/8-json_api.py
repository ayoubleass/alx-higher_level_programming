#!/usr/bin/python3
"""This script t takes in a letter and
sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter."""


if __name__ == "__main__":
    import sys
    import requests
    url = " http://0.0.0.0:5000/search_user"
    par = sys.argv[1] if len(sys.argv) > 1 else ""
    r = requests.post(url, data={"q": par})
    try:
        result = r.json()
        if len(result) == 0:
            print("No result")
        else:
            print("[{}] {}".format(result.get('id'), result.get('name')))
    except ValueError:
        print("Not a valid JSON")
