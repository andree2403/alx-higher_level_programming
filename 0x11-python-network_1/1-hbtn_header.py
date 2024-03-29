#!/usr/bin/python3
""" a Python script that takes in a URL, sends a request"""
import sys
import urllib.request

if __name__ == "__main__":
    req = sys.argv[1]
    with urllib.request.urlopen(req) as response:
        ans = response.read()
        print(dict(response.headers).get("X-Request-Id"))
