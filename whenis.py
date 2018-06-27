#!/usr/bin/env python3
# -*- encoding  utf-8 -*-
from datetime import datetime as dt, timedelta
import sys

# convert unix timestamp(with microseconds) into readable time
if len(sys.argv) >= 2:
    atime = sys.argv[1]
    atime_ms = 0
    if not atime.isdecimal():
        if atime == 'now':
            print(dt.now().timestamp())
        else:
            try:
                print(dt.strptime(atime, '%Y%m%d_%H%M%S').timestamp())
            except:
                print("[ERROR]: Date not in format YYYYmmdd_HHMMSS:", atime)
        exit(0)
    if len(atime) > 10:
        atime_ms = int(atime[10:])
        atime = atime[0:10]
    atime = int(atime)
    adate = dt.fromtimestamp(atime)
    adate += timedelta(microseconds=atime_ms*1000)
    print(adate)
else:
    print('[ERROR]: Ask me do something, PLEASE!')
