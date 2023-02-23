#!/usr/bin/python3
"""Adds all argument to a python list and saves it to file"""


import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    items = load_from_json_file("add_item.json")
except FileNotFoundError:
    item = str(sys.argv[1:])
    save_to_json_file(item, "add_item.json")
