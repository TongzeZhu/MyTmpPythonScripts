#!/usr/bin/env python3
# -*- encoding utf8 -*-

import imghdr
import sys
if len(sys.argv) == 0:
    exit(0)
else:
    for i in range(1, len(sys.argv)):
        print(sys.argv[i], " is of format ", imghdr.what(sys.argv[i]))

