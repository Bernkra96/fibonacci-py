# Fibonacci sequence
import sys
import time


A = 0  # Start Val A B 
B = 1

runFor = 10000 #nOfRuns

limString = 0 #set limit for int to string conversion // 0 for unlimited

sys.set_int_max_str_digits(limString)

startTime = time.time() #Start Time 

for i in range(runFor):
     
     C = A + B
   
       
     print(C)
     B = A
     A = C

endTime = time.time()      #END Time 
print('┌─────────────────────────────────────────────────────────')
print('│','Set Number of Runs:',runFor,)
print('│','Run Number of Runs:',i+1,)
print('├─────────────────────────────────────────────────────────')
print('│','Start Time',startTime,'End Time',endTime,)
print('│','Run Time seconds',endTime - startTime,)
print('└─────────────────────────────────────────────────────────')
time.sleep(0)