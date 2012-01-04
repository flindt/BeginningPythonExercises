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


def tick():
    '''
    returns a new time for each tick of the signal
    '''
    
    # using "yield" a function can return a value without losing the state it is in
    # next time the function is called it will resume (start again) right after the "yield"
    yield 0.0
    yield 0.001
    yield 0.002


def signal(t):
    return 0.0



def write_to_file(output_filename="output.dat", signals = ()):
    '''
    open the output file, generates the time and signals by calling the respective functions
    the parameter outputfilename allows the caller to set the output filename
    
    '''
    file_handle = open(output_filename,'w')
    file_handle.write("time / ms \toutput / V\n")
    
    for t in tick():
        print("%f \t%f"%(t, signal(t) ))
        file_handle.write("%f \t%f\n"%(t, signal(t) ))
    
    
    file_handle.close()
    
    
    
    
write_to_file()


