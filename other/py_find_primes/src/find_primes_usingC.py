'''
Created on Dec 14, 2011

@author: pfl
'''


import ctypes
ctypes.cdll.LoadLibrary("/home/pfl/git/beginning_C/other/find_primes/Debug/lib_primes.so")
libc = ctypes.CDLL("/home/pfl/git/beginning_C/other/find_primes/Debug/lib_primes.so")

libc.optimised_1(1000000)