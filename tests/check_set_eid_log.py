#!/usr/bin/env python3
'''Regression test for SetEID rejected debug log argument order.'''
import sys

SOURCE = 'ctrld/mctp-discovery.c'


def main():
    with open(SOURCE) as f:
        lines = f.readlines()

    # Find the MCTP_CTRL_DEBUG call that logs the rejected SetEID response.
    for start, line in enumerate(lines):
        if 'MCTP_CTRL_DEBUG' not in line:
            continue
        block = ''
        for j in range(start, min(start + 10, len(lines))):
            block += lines[j]
            if ');' in lines[j]:
                break
        if 'Rejected by the device' in block:
            if '__func__, set_eid_resp->eid_set, set_eid_resp->status' in block:
                print('OK: SetEID rejected log arguments are in the correct order')
                return 0
            print('ERROR: wrong argument order in SetEID rejected log', file=sys.stderr)
            return 1

    print('ERROR: SetEID rejected log call not found', file=sys.stderr)
    return 1


