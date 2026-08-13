#!/bin/sh
# Regression check: mctp-discovery.c uses assert(0), so it must
# explicitly include <assert.h> rather than relying on transitive headers.
if ! grep -q '^#include <assert.h>$' ctrld/mctp-discovery.c; then
	echo "Missing <assert.h> include in ctrld/mctp-discovery.c" >&2
	exit 1
