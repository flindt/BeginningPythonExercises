'''
Created on Jan 4, 2012

@author: pfl
'''



def read_from_file( input_file_name = "output.dat"):
    input_signal = []
    
    file_handle = open( input_file_name, 'r')
    
    for this_line in file_handle.readlines():
        try:
            input_signal.append( (float(this_line.split()[0]), float(this_line.split()[1])) )
        except (ValueError,IndexError):
            pass
        
    
    file_handle.close()
    return input_signal

def ex_2_1(input_file_name = "output.dat"):
    return len( read_from_file(input_file_name))

def ex_2_2(input_file_name = "output.dat"):
    max = 0.0
    min = 9e9
    for this_value in read_from_file(input_file_name):
        if max < this_value[1]:
            max = this_value[1]
        if min > this_value[1]:
            min = this_value[1]
    return (min,max)

print (ex_2_1())
print (ex_2_2())