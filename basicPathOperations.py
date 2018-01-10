#!/usr/bin/python3
# -*- encoding utf-8 -*-
# #finished
import os

def printPathParts(filePath = '~/noexist/a_folder/a_file'):
    print("filename is ", os.path.basename(filePath))
    print("directory path is ", os.path.dirname(filePath))
    print("directory name is ", os.path.basename(os.path.dirname(filePath)))
    print("after expand ~ to user home directory, whole path is ", os.path.expanduser(filePath))
    print("the relative path of this path is ", os.path.relpath(os.path.expanduser(filePath)))
    print()

def printCurPathParts():
    print("current working directory is ", os.path.abspath(os.path.curdir))
    print("which is the same as ", os.path.curdir)
    print()
    
def splitPath(filePath0="/home/me/b_folder//", filePath1="/home/me/b_folder/b_file"):
    print("split result for ", filePath0, " is ", os.path.split(filePath0), " ", sep='"');
    print("split result for ", filePath1, " is ", os.path.split(filePath1), " ", sep='"');
    print()

def joinPath(filePath="/home/me/", part0="folder1/", part1="folder2/", part2="../anotherFolder/", part3="a_file", part4="/home/me/newFolder/absPath/will/clean/all/"):
    print("first join result: ", os.path.join(filePath, part0, part1, part2, part3))
    print("second join result: ", os.path.join(filePath, part4))
    print()

def cleanPathSep(filePath="/home//me/folder1//file/"):
    print("before normalization is ", filePath, " after that is ", os.path.normpath(filePath), "", sep='"')
    print()



printPathParts()
printCurPathParts()
splitPath()
joinPath()
cleanPathSep()
