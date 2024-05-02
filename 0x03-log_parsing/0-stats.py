#!/usr/bin/python3
'''Log parsing'''

import re
from sys import stdin

i = 0
total_size = 0
codes = {'200': 0, '301': 0, '400': 0, '401': 0,
         '403': 0, '404': 0, '405': 0, '500': 0}

try:
    for line in stdin:

        line_pattern = re.compile(
            r"(\d{1,4})\.(\d{1,4})\.(\d{1,4})\.(\d{1,4}) "
            r"\- \[(\d{4}\-\d{2}\-\d{2} \d{2}\:\d{2}\:\d{2}\.\d+)\] "
            r"\"GET \/projects\/260 HTTP\/1\.1\" (\d{3}) (\d+)")
        match = line_pattern.match(line)

        if match:
            # ip = ".".join(match.groups()[0: 4])
            status_code = match.groups()[-2]
            file_size = int(match.groups()[-1])
            # print(f'{status_code} : {file_size}')

            if status_code in codes.keys():
                codes[status_code] = codes[status_code] + 1
            total_size += file_size

        if i > 10:
            break
        i += 1

        print('File size: {}'.format(total_size))
        for code, value in codes.items():
            if value != 0:
                print('{}: {}'.format(code, value))

except KeyboardInterrupt:
    if status_code in codes.keys():
        codes[status_code] = codes[status_code] + 1
        total_size += file_size
    print('File size: {}'.format(total_size))
    for code, value in codes.items():
        if value != 0:
            print('{}: {}'.format(code, value))
