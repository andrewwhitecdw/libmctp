#!/usr/bin/env python3
'''Regression test for redundant msg_type_table.enabled assignment.'''
import re
import sys

SRC = 'ctrld/mctp-discovery-i2c.c'

def main():
    with open(SRC, encoding='utf-8') as f:
        text = f.read()
    matches = re.findall(r'msg_type_table\.enabled = true;', text)
    if len(matches) != 1:
        print('ERROR: expected exactly one msg_type_table.enabled = true, found', len(matches))
        return 1
    print('OK')
    return 0

if __name__ == '__main__':
