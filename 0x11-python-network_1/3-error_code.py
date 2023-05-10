#!/usr/bin/python3
"""A script that:
- takes in a URL,
- sends a request to the URL
- displays the body of the response (decoded in utf-8).
"""

import sys
from urllib import request, error

if __name__ == "__main__":
    req = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(req) as response:
            html = response.read()
            print(html.decode("UTF-8"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
