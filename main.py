#!/usr/bin/env python2
import sys


def main():
    args = sys.argv
    if len(args) == 1:
        exit()
    prevContents = ""
    for i in range(1, len(args) - 1):
        with open(args[i], 'r') as book:
            prevContents += book.read() + '\n'
    with open(args[-1], 'w') as f:
        f.write(prevContents)


main()
