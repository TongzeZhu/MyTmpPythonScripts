#!/usr/bin/env python3
# -*- encoding utf8 -*-
import inspect

def log1(msg):
    # 1 represent caller, 2 represent index of lineno in tuple 
    line = inspect.stack()[1][2]
    # TODO: SHOULD get outer frame
    aframe = inspect.currentframe()
    line2 = inspect.getframeinfo(aframe, 0)[1]
    # frame object must be deleted, or program will be slowed down
    del aframe
    print(type(line2))
    print(msg, 'line', line, line2)


if __name__ == '__main__':
    log1('We call FUNC log1 from')
