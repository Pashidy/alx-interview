#!/usr/bin/python3
import random
import sys
from time import sleep
import datetime

for i in range(10000):
    sleep(random.random())

    # Format string for output
    format_string = (
        "{:s} - [{}] \"GET /projects/260 HTTP/1.1\" {} {}\n"
    )

    # Generate random IP address
    ip = "{:d}.{:d}.{:d}.{:d}".format(
        random.randint(1, 255),
        random.randint(1, 255),
        random.randint(1, 255),
        random.randint(1, 255)
    )
    # Get current timestamp
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Generate random status code and file size
    status_code = random.choice([200, 301, 400, 401, 403, 404, 405, 500])
    file_size = random.randint(1, 1024)

    # Write formatted output
    sys.stdout.write(format_string.format(
        ip, timestamp, status_code, file_size
    ))
    sys.stdout.flush()
