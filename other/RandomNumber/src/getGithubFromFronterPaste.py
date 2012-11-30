'''
Created on Sep 20, 2012

@author: flindt
'''


import csv

headerNames = ['a','b','c','d']
pastefile = open('pastefromfronter','r',encoding="utf-8")
csvRead = csv.DictReader( pastefile, headerNames, delimiter="\t")

for line in csvRead:
    print( line )