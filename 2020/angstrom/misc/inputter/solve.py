#!/usr/bin/env python2

from pwn import *

p = process(["./inputter", " \n'\"\x07"])
p.sendline("\x00\x01\x02\x03")
print(p.recvall(timeout=2))
