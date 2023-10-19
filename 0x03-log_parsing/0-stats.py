#!/usr/bin/python3
"""
This module reads stdin line by line and
computes metrics
"""
from sys import stdin


def print_stats(dict_code_stat, file_size):
    """a function to print the status in a format"""
    print("File size: {}".format(file_size))
    for k, v in sorted(dict_code_stat.items()):
        if v != 0:
            print("{}: {}".format(k, v))


file_size = 0
code_stat = 0
count = 0
dict_code_stat = {"200": 0,
                  "301": 0,
                  "400": 0,
                  "401": 0,
                  "403": 0,
                  "404": 0,
                  "405": 0,
                  "500": 0}

try:
    for line in stdin:
        entered_line = line.split()  # splits read line
        entered_line = entered_line[::-1]  # inverts the splitted line

        if len(entered_line) > 2:
            count += 1

            if count <= 10:
                file_size += int(entered_line[0])  # the file size
                code_stat = entered_line[1]  # status code

                if (code_stat in dict_code_stat.keys()):
                    dict_code_stat[code_stat] += 1

            if (count == 10):
                print_stats(dict_code_stat, file_size)
                count = 0
finally:
    print_stats(dict_code_stat, file_size)
