# Fibonacci sequence
import sys
import time


A = 0  # Start Val A B 
B = 1
global runFor 
global inputVal 


limString = 0 #set limit for int to string conversion // 0 for unlimited

def setup():
     global runFor 
     global inputVal 
     print('Hallo Welcome')
     print('Set Number off runs ')
     
     inputVal = input()
     
    
     if   any(char.isdigit() for char in inputVal) is True:
           print("Is Valid InT") 
     else :

          print("Is not Valid InT")     
          sys.exit()
          
     inputVal = int(inputVal)
     
     

     

     

    
    
    
    
     runFor = inputVal
     print('Runs Fibonacci.Set to',runFor,'times')
   





def calc():  
     global A
     global B
     
     global i
     global startTime
     global endTime
     startTime = time.time() #Start Time 
     for  i in range(runFor):
     
          C = A + B
       
          print(C)
          B = A
          A = C


     endTime = time.time() 
 
 #END Time 





def printResult(): 
      
     if 'i' in globals() or 'i' in locals() :
        

          print('┌─────────────────────────────────────────────────────────'),
          print('│','Set Number of Runs:',runFor,),
          print('│','Run Number of Runs:',i+1,),
          print('├─────────────────────────────────────────────────────────'),
          print('│','Start Time',startTime,'End Time',endTime,),
          print('│','Run Time seconds',endTime - startTime,),
          print('└─────────────────────────────────────────────────────────')
     elif  runFor == 0 or inputVal is None: 
          print('Error No Run. "Run for N" to wars Set to 0')
     else: 
          print('Error No Run.')

     
    

setup()
calc()
printResult()    
time.sleep(5)