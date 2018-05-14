#!/usr/bin/env python3
# -*- encoding utf8 -*-

from scipy import misc
import numpy


def combineImage():
    a = misc.imread("/home/tongze/testspace/testCombine.jpg")
    # print(a.shape)
    c = a[:, :int(a.shape[1]/2), :].copy()
    for i in 0,4:
        # there are two braces after hstack
        c = numpy.hstack((c,a[:, int(a.shape[1]/2-100):512, :]))
    savePath = '/home/tongze/testspace/combineImage.jpg'
    misc.imsave(savePath, c)
    print('New combined image saved to', savePath)

def cutMidOfImage():
    a = misc.imread("/home/tongze/testspace/testCut.jpg") 
    # print(a.shape)
    c = a[200:1300, 200:1200, :].copy()
    savePath = '/home/tongze/testspace/midImage.jpg'
    misc.imsave(savePath, c)
    print('New cut image saved to', savePath)

combineImage()
cutMidOfImage()
