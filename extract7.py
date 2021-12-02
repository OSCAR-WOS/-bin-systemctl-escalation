#!/usr/bin/env python3
new_file = open('extract7.txt', 'w')

with open('100k.txt', 'r') as f:
    lines = f.readlines()

    for line in lines:
        if len(line.strip()) == 7:
            new_file.write(line)


new_file.close()
