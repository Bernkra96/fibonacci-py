"""Fibonacci sequence"""

import sys
import time


# Start Val A B s
A = 0
B = 1
global runFor 
global inputVal 
#Options preset
optionsDataSet = {"EndTimer": True,"TimeEndTimer": 2
}

#Limit for int to string conversion
limString = 0 #set limit for int to string conversion // 0 for unlimited
sys.set_int_max_str_digits(limString) 
def setup():
     global runFor 
     global inputVal 
     print('─────────────────────────────────────────────────────────'),
     print('Hallo Welcome.')
     print('To this Fibonacci Runner / Benchmark.')
     print('Set Number off runs.')
     print("o for options, s for set up ") 
     
     inputVal = input("Number or text(Listed Only).: ")
     
    
     if   any(char.isdigit() for char in inputVal) is True:
           print("Is Valid InT.") 
           inputVal = int(inputVal)
     elif any(char.lower() == 'o' for char in inputVal):

          options()     
     elif any(char.lower() == 's' for char in inputVal):
          for x in optionsDataSet:
           
           updateSetting(optionsDataSet , x )    

           
          setup()     
     else :

           print("Is not Valid InT.")     
           sys.exit()
          
      
      
   
     
     

     

     

    
    
    
    
     runFor = inputVal
     print(f'Runs Fibonacci.Set for {runFor} times.')
   
     
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
        

          print(f'┌─────────────────────────────────────────────────────────'),
          print(f'│ Set Number of Runs: {runFor}'),
          print(f'│ Run Number of Runs: {i+1}'),
          print(f'├─────────────────────────────────────────────────────────'),
          print(f'│ Start Time {startTime} End Time {endTime}'),
          print(f'│ Run Time seconds {endTime - startTime}'),
          print(f'└─────────────────────────────────────────────────────────')
     elif  runFor == 0 or inputVal is None: 
          print(f'Error No Run. "Run for N" to wars Set to 0.')
     else: 
          print(f'Error No Run.')


def options():
     print("Options") 
     print("e for exit,h for help,i for info,u for update") 
     inputVal = input("Text(Listed Only).: ")
     
     if any(char.lower() == 'e' for char in inputVal):
          setup()
     elif  any(char.lower() == 'h' for char in inputVal):
          print('Help')  
          print('o = Options')  
          print('Opens Options ')
          print('e = Exit ')  
          print('Exit Options ')  
          print('u = Exit ')  
          print(f'Update Options')    
          options()   
     elif  any(char.lower() == 'i' for char in inputVal):
          print('Info')  
          print(optionsDataSet) 
          options() 
     elif  any(char.lower() == 'u' for char in inputVal):
          print('Update')  
          updaterOptions()     
     else :

          print("Is not Valid ")     
          sys.exit()
          

def updaterOptions():
    
     
     print("Update witch Option ?")
     print(optionsDataSet) 
     selectOptionsUserInput = input("Text(Option Name).: ")
   
     if selectOptionsUserInput in optionsDataSet:
        print(selectOptionsUserInput,optionsDataSet[selectOptionsUserInput] )
     else: 
          print("No Valet input")
        
     
     options() 
     
   
     
     
     

def updateSetting(name , key ):    
   
     match name[key]:
          case bool():
              print("Is a BoolStetting")
              print('Name of Setting{key}and is, {name[key]}')
          

          case int():
              print("Is IntSetting")
              print('Name of Setting{key}and is, {name[key]}')
          case _:
               print("Error No Valid Format ")

     


          
     

setup()
calc()
printResult()
#EndTimer
if optionsDataSet["EndTimer"] == True :
     time.sleep(optionsDataSet["TimeEndTimer"])