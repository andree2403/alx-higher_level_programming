#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary or len(a_dictionary) == 0:
        return None
    best_key = max(a_dictionary, key = a_dictionary.get)
    return best_key
