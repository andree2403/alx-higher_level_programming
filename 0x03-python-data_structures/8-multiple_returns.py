#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    first = sentence[0]
    if len(sentence) == 0:
        sentence[0] == None
    return (length, first)
