'''
Created on Jan 4, 2012

@author: pfl
'''

signal_types = (ZERO, NOISE, SINUS) = (0,1,2)

# Define start and end time, and the time step
# The unit used is seconds 
t_start = 0.0
t_end = 1.0
t_step = 0.001  


def t():
    '''
    returns a new time for each tick of the signal
    '''
    yield 0.0


def signal():
    pass



def write_to_file():
    pass


