#!/usr/bin/python3
"""
A script that reads stdin line by line and computes metrics.
"""
import sys
import signal


def print_msg(dict_sc, total_file_size):
    """
    Method to print statistics.

    Args:
        dict_sc: Dictionary of status codes and their counts.
        total_file_size: Total size of all files processed.
    """
    print("File size: {}".format(total_file_size))
    for key, val in sorted(dict_sc.items()):
        if val != 0:
            print("{}: {}".format(key, val))

total_file_size = 0
counter = 0
dict_sc = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}


def signal_handler(sig, frame):
    """
    Handle the interrupt signal to print the final statistics.
    """
    print_msg(dict_sc, total_file_size)
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        parsed_line = line.split()
        if len(parsed_line) != 10:
            continue

        counter += 1
        total_file_size += int(parsed_line[-1])
        code = parsed_line[-2]

        if code in dict_sc:
            dict_sc[code] += 1

        if counter == 10:
            print_msg(dict_sc, total_file_size)
            counter = 0

except KeyboardInterrupt:
    print_msg(dict_sc, total_file_size)
    sys.exit(0)

# Print any remaining statistics when the script ends naturally
print_msg(dict_sc, total_file_size)
