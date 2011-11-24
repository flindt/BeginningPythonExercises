'''
Created on Nov 24, 2011

@author: pfl
'''


import Ch8

# try out the functions in the code from the book
Ch8.print_dir(".")
# Ch8.print_dir_by_ext(".")  # seems broken, TODO: fix this
Ch8.print_line_lengths()
print(Ch8.split_fully("/home/user/workspace"))
Ch8.print_tree("../../")
Ch8.print_dir_info("../../")
print(Ch8.make_version_path("./testbin","1.001"))
# Ch8.rotate("./test.txt", 3) #only works if the file "test.txt.3 exists
