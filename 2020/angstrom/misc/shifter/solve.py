#!/usr/bin/env python2

from pwn import *

def fibonacci(n):
    a,b = 0,1
    for i in range(n):
        a,b = b,a+b
    return a

def generate_fibs(max_fib):
    mapping = {}
    for i in range(max_fib):
        mapping[i] = fibonacci(i)

    return mapping

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def encipher(ciphertext, shift):
    shift = shift % 26
    ret = ""

    for c in ciphertext:
        ret += letters[(ord(c) - ord('A') + shift) % 26]

    return ret

def solve():
    # Calculate fibonacci before connecting because we are timed
    mappings = generate_fibs(50)

    p = remote("misc.2020.chall.actf.co", 20300)
    p.recvlines(6)

    while True:
        line = p.recvline().split(' ')
        print(line)
        cipher = line[-3]
        fib = int(line[-1][2:-1])
        p.sendline(encipher(cipher, mappings[fib]))


solve()

# Flag: actf{h0p3_y0u_us3d_th3_f0rmu14-1985098}
