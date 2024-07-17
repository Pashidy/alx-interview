#!/usr/bin/python3
"""
A script that reads stdin line by line and computes metrics.
"""
import sys
import signal

def printsts(dic, size):
    """
    Prints information
    """
    print("File size: {:d}".format(size))
    for key in sorted(dic.keys()):
        if dic[key] != 0:
            print("{}: {:d}".format(key, dic[key]))

sts = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0,
       "404": 0, "405": 0, "500": 0}

count = 0
size = 0

def signal_handler(sig, frame):
    """
    Handle the interrupt signal to print the final statistics
    """
    printsts(sts, size)
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        stlist = line.split()

        if len(stlist) < 2:
            continue

        count += 1

        try:
            size += int(stlist[-1])
        except ValueError:
            pass

        if stlist[-2] in sts:
            sts[stlist[-2]] += 1

        if count % 10 == 0:
            printsts(sts, size)

except KeyboardInterrupt:
    printsts(sts, size)
    raise

printsts(sts, size)
