'''
Created on Jun 21, 2019

@author: AAbdelaziz
'''
import random
import os
from fractions import Fraction
def main():
     #f=open("Test.txt", "a+")
    
     #remove_newlines("Test.txt")
#     Fileinfo = os.stat('Test.txt')
#     SizeKB= round((Fileinfo.st_size /1024.0),1) 
#     print(SizeKB) 
#     
#     if SizeKB == 10.0:
#         print("File Size is 10 KB")
#     
#     infile = open("Test.txt", "r")
#     data = infile.read()[random.randint(0,2):(Fileinfo.st_size)]
#     print (data)
#     infile.close()
#     
#     
#     infile = open("Test.txt", "w")
#     infile.write(data)
#     infile.close()
    val=Fraction(0.5)
    print(val*1024.0)

def remove_newlines(fname):
    flist = open(fname).readlines()
    return [s.rstrip('a') for s in flist]

if __name__ == '__main__':
    main()