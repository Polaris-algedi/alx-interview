#!/usr/bin/python3
"""
This module provides functions to parse log files and print statistics.

The module contains the following functions:
- print_statistics(status_dict, file_size): Prints the statistics
of the log file.
- get_file_size(line): Gets the file size from a log line.
- get_status_code(line): Gets the status code from a log line.
- log_parsing(): Parses the log file and prints statistics.
"""

import sys
import re


def print_statistics(status_dict, file_size):
    """
    Print the statistics of the log file.

    Args:
        status_dict (dict): A dictionary containing the count
        of each status code.
        file_size (int): The total file size.

    Returns:
        None
    """
    print('File size: {}'.format(file_size))
    status_codes = [200, 301, 400, 401, 403, 404, 405, 500]
    for code in status_codes:
        if status_dict[code] != 0:
            print('{}: {}'.format(code, status_dict[code]))


status_dict = {
    200: 0, 301: 0,
    400: 0, 401: 0,
    403: 0, 404: 0,
    405: 0, 500: 0
}
total_size = 0
count = 1
try:
    for line in sys.stdin:
        if line.count(' ') != 8:
            continue
        try:
            # Get the file size from a log line.
            file_size = re.search(r'\d+$', line)
            total_size += int(file_size.group())

            # Get the status code from a log line.
            status_code_match = re.search(
                r' 200|301|400|401|403|404|405|500 ', line)
            status_code = int(status_code_match.group())
            status_dict[status_code] += 1
        except (TypeError, AttributeError, ValueError):
            continue

        if count == 10:
            print_statistics(status_dict, total_size)
            count = 1
        else:
            count += 1
except KeyboardInterrupt:
    print_statistics(status_dict, total_size)
