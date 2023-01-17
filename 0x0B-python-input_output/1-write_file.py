#!/usr/bin/python3

def write_file(filename="", text=""):
    return open(filename, 'w', encoding='utf8').write(text)
