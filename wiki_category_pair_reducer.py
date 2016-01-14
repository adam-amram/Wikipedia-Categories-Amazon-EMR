#!/usr/bin/env python

import sys
import os

block_key = None
count = 0

for line in sys.stdin:
    line = line.strip()
    key = line
    if key != block_key:
        if block_key != None and count > 1:
            print block_key, count
        count = 0
        block_key = key
    count += 1
if block_key != None and count > 1:
    print block_key, count
