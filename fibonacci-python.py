# Fibonacci sequence
import sys
import time


A = 0  # Start Val A B s

B = 1
global runFor 
global inputVal 
#Options preset
optionsData = {"EndTimer": True,"EndTimerTime": 1,
}


limString = 0 #set limit for int to string conversion // 0 for unlimited

def setup():
     global runFor 
     global inputVal 
     print('─────────────────────────────────────────────────────────'),
     print('Hallo Welcome.')
     print('To this Fibonacci Runner / Benchmark.')
     print('Set Number off runs.')
     print("o for options,s for set up ") 
     
     inputVal = input()
     
    
     if   any(char.isdigit() for char in inputVal) is True:
           print("Is Valid InT.") 
           inputVal = int(inputVal)
     elif any(char.lower() == 'o' for char in inputVal):

          options()     
     elif any(char.lower() == 's' for char in inputVal):
          for x in optionsData:
           print (x, optionsData[x]  )  
           
          setup()     
     else :

           print("Is not Valid InT.")     
           sys.exit()
          
      
      
   
     
     

     

     

    
    
    
    
     runFor = inputVal
     print('Runs Fibonacci.Set to',runFor,'times.')
   
 
     



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
          print('Error No Run. "Run for N" to wars Set to 0.')
     else: 
          print('Error No Run.')


def options():
     print("Options") 
     print("e for exit,h for help,i for info") 
     inputVal = input()
     
     if any(char.lower() == 'e' for char in inputVal):
          setup()
     elif  any(char.lower() == 'h' for char in inputVal):
          print('Help')  
          print('o = Options')  
          print('Opens Options ')
          print('e = Exit ')  
          print('Exit Options ')    
          options()   
     elif  any(char.lower() == 'i' for char in inputVal):
          print('Info')  
          print(optionsData) 
          options()    
     else :

          print("Is not Valid ")     
          sys.exit()
          
          
     

setup()
calc()
printResult()
#EndTimer
if optionsData["EndTimer"] == True :
     time.sleep(optionsData["EndTimerTime"])