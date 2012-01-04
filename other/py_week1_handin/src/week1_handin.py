'''
Created on Jan 4, 2012

@author: pfl
'''

import random
import math

signal_types = (ZERO, NOISE, SINUS) = (0,1,2)

# Define start and end time, and the time step
# The unit used is seconds 
t_start = 0.0
t_end = 1.0
t_step = 0.001  


def tick():
    '''
    returns a new time for each tick of the signal
    '''
    
    # using "yield" a function can return a value without losing the state it is in
    # next time the function is called it will resume (start again) right after the "yield"
#    yield 0.0
#    yield 0.001
#    yield 0.002
    t_now = t_start
    while t_now < t_end:
        t_now = t_now + t_step
        yield t_now
    

def zero(t):
    return 0.0

def noise(t):
    # random gives a number from 0 to one, here a number from -1 to 1 is needed
    return random.random() * 2 - 1

def sinus(t, freq = 50):
    return math.sin( 2*math.pi* t * freq)
    

def signal(t, signals):
    total_signal = 0
    for this_signal in signals:
        if this_signal == ZERO:
            total_signal = total_signal + zero(t)
        if this_signal == NOISE:
            total_signal = total_signal + noise(t)
        if this_signal == SINUS:
            total_signal = total_signal + sinus(t)
               
    return total_signal


def write_to_file(output_filename="output.dat", signals = (ZERO, )):
    '''
    open the output file, generates the time and signals by calling the respective functions
    the parameter outputfilename allows the caller to set the output filename
    
    '''
    file_handle = open(output_filename,'w')
    file_handle.write("time / ms \toutput / V\n")
    
    for t in tick():
        file_handle.write("%f \t%f\n"%(t, signal(t, signals) ))
    
    file_handle.close()
    
    
# notide the comma ',' after the signal name. This is to make python understand that we need a tuple with just one element.
# (ZERO) will be seen as an constant in a parentheses -> ZERO
# (ZERO,) -> (ZERO)        that is a tuple
write_to_file("output_zero.dat", (ZERO,))
write_to_file("output_sinus.dat", (SINUS,))


