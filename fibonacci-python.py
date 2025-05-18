# Fibonacci sequence
import sys

A = 0  # Start Val A B 
B = 1

runFor = 500 #nOfRuns

limString = 0 #set limit for int to string conversion // 0 for unlimited

sys.set_int_max_str_digits(limString)

for i in range(runFor):
     
     C = A + B
   
       
     print(C)
     B = A
     A = C
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('Set Number of Runs:',runFor)
print('Run Number of Runs:',i+1)