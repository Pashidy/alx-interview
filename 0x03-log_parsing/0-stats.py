#!/usr/bin/python3
"""
A script that reads stdin line by line and computes metrics.
"""
import sys
import signal

total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0


def print_statistics():
    """
    To show stats
    """
    global total_size, status_codes
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


def signal_handler(sig, frame):
    """
    To send signals
    """
    print_statistics()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        line_count += 1

        parts = line.split()
        if len(parts) < 10:
            continue

        ip = parts[0]
        dash = parts[1]
        date = parts[2] + ' ' + parts[3] + ' ' + parts[4]
        request = parts[5] + ' ' + parts[6] + ' ' + parts[7]
        status_code = parts[8]
        file_size = parts[9]

        if not status_code.isdigit() or not file_size.isdigit():
            continue

        status_code = int(status_code)
        file_size = int(file_size)

        total_size += file_size
        if status_code in status_codes:
            status_codes[status_code] += 1

        if line_count % 10 == 0:
            print_statistics()

except KeyboardInterrupt:
    print_statistics()
    sys.exit(0)
