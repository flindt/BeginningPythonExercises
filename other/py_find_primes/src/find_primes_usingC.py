'''
Created on Dec 14, 2011

@author: pfl
'''


'''

In order to use a shared library written in C you will have to compile it first:
    
    gcc -c find_primes.c
    gcc -shared -o lib_primes.so find_primes.o
    
Then you can open it from within python, if you use the complete path for it.

http://richizo.wordpress.com/2009/01/25/calling-c-functions-inside-python/
'''



import ctypes
#ctypes.cdll.LoadLibrary("/home/pfl/git/beginning_C/other/find_primes/Debug/lib_primes.so")
#libc = ctypes.CDLL("/home/pfl/git/beginning_C/other/find_primes/Debug/lib_primes.so")
ctypes.cdll.LoadLibrary("../c_src/lib_primes.so")
libc = ctypes.CDLL("../c_src/lib_primes.so")

libc.optimised_1(1000000)