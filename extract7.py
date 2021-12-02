#!/usr/bin/env python3
new_file = open('extract7.txt', 'w')

with open('100k.txt', 'r') as f:
    lines = f.readlines()

    for line in lines:
        if len(line) is 7:
            new_file.write(f'{line}')


new_file.close()
