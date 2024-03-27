#!/usr/bin/python3
"""
This module provides functions to parse log files and print statistics.

The module contains the following functions:
- print_statistics(status_dict, file_size): Prints the statistics
of the log file.
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
    print('File size:', file_size)
    for code, count in sorted(status_dict.items()):
        if count:
            print(f"{code}: {count}")


status_dict = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
total_size = 0
count = 0

try:
    for line in sys.stdin:
        # Extract file size and status code
        file_size_match = re.search(r'\b(\d+)\s*$', line)
        status_code_match = re.search(
            r'\b(200|301|400|401|403|404|405|500)\b', line)

        if file_size_match and status_code_match:
            file_size = int(file_size_match.group(1))
            total_size += file_size

            status_code = int(status_code_match.group(1))
            status_dict[status_code] += 1

            count += 1
            if count == 10:
                print_statistics(status_dict, total_size)
                count = 0

except KeyboardInterrupt:
    print_statistics(status_dict, total_size)
