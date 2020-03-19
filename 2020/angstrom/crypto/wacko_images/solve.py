#!/usr/bin/env python2

from numpy import *
from PIL import Image

# Given to us
def enc():
    flag = Image.open(r"flag.png")
    img = array(flag)

    key = [41, 37, 23]

    a, b, c = img.shape

    for x in range (0, a):
        for y in range (0, b):
            pixel = img[x, y]
            for i in range(0,3):
                pixel[i] = pixel[i] * key[i] % 251
            img[x][y] = pixel

    enc = Image.fromarray(img)
    enc.save('enc.png')

# Naive way to calculate this inverse since i has to be in range [0, 255]
def stupid_inverse(key, new_pix, mod) : 
    for i in range(256):
        if (((i * key) % mod) == new_pix):
            return i

    return -1

# Inverse of enc function which was given
def dec():
    flag = Image.open("enc.png")
    img = array(flag)

    key = [41, 37, 23]

    a, b, c = img.shape

    for x in range (0, a):
        for y in range (0, b):
            pixel = img[x, y]
            for i in range(0,3):
                temp = stupid_inverse(key[i], pixel[i], 251)
                if temp == -1:
                    return

                pixel[i] = temp

            img[x][y] = pixel

    enc = Image.fromarray(img)
    enc.save('flag.png')

dec()
