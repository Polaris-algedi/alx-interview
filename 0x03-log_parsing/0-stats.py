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
    for key in status_dict:
        if status_dict[key] != 0:
            print('{}: {}'.format(key, status_dict[key]))


def log_parsing():
    """
    Parse the log file and print statistics.

    Returns:
        None
    """
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
            # Get the file size from a log line.
            file_size = re.search(r'\d+$', line)
            total_size += int(file_size.group())

            # Get the status code from a log line.
            status_code_match = re.search(
                r' 200|301|400|401|403|404|405|500 ', line)
            if status_code_match:
                status_code = int(status_code_match.group())
                status_dict[status_code] += 1

            if count == 10:
                print_statistics(status_dict, total_size)
                count = 1
            else:
                count += 1
    except KeyboardInterrupt:
        print_statistics(status_dict, total_size)


log_parsing()
