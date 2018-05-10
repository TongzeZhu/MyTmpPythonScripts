#!/usr/bin/python3
# -*- encoding utf8 -*-

from scipy import misc
import numpy


def combineImage():
    a = misc.imread("/home/tongze/test.jpg")
    print(a.shape)
    c = a[:, :int(a.shape[1]/2), :].copy()
    for i in 0,4:
        # there are two braces after hstack
        c = numpy.hstack((c,a[:, int(a.shape[1]/2-100):512, :]))
    misc.imsave('test.jpg', c)

combineImage()
