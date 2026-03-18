"""Fibonacci sequence"""


import sys
import time


# Start Val A B s
A = 0
B = 1
global runFor 
global inputVal 
#Options preset
optionsDataSet = {"EndTimer": True,"TimeEndTimer": 2 , "PrintEndResult" : True , "SaveEndResult" : True
               
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

     while True:
          inputVal = input("Number or text(Listed Only).: ")
     
    
          if   any(char.isdigit() for char in inputVal) is True:
           print("Is Valid InT.") 
           inputVal = int(inputVal)
           
           runFor = inputVal
           print(f'Runs Fibonacci.Set for {runFor} times.')
           break
           
          elif any(char.lower() == 'o' for char in inputVal):

                options()    
                break 
          elif any(char.lower() == 's' for char in inputVal):
           
           print(optionsDataSet)   
           
           setup()  
           break
           
          else :

           print("Is not Valid InT.")     
           
          
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
     
     if 'i' in globals() and optionsDataSet["PrintEndResult"] == True or 'i' in locals() and optionsDataSet["PrintEndResult"] == True:
        

          print(f'┌─────────────────────────────────────────────────────────'),
          print(f'│ Set Number of Runs: {runFor}'),
          print(f'│ Run Number of Runs: {i+1}'),
          print(f'├─────────────────────────────────────────────────────────'),
          print(f'│ Start Time {startTime} End Time {endTime}'),
          print(f'│ Run Time seconds {endTime - startTime}'),
          print(f'└─────────────────────────────────────────────────────────')
     elif  runFor == 0 or inputVal is None: 
          print(f'Error No Run. "Run for N" to wars Set to 0.') 
   
     if 'i' in globals() and optionsDataSet["SaveEndResult"] == True or 'i' in locals() and optionsDataSet["SaveEndResult"] == True:
          resultFile = open("result.txt", "w",encoding='utf-8')
         
          print(f'┌──────────────────────────────────────────────────────────────────────────', file=resultFile ),
          print(f'│ Fibonacci Runner / Benchmark Result',file=resultFile )
          print(f'├──────────────────────────────────────────────────────────────────────────',file=resultFile ), 
          print(f'│ Set Number of Runs: {runFor}', file=resultFile ),
          print(f'│ Run Number of Runs: {i+1}',file=resultFile ),
          print(f'├──────────────────────────────────────────────────────────────────────────',file=resultFile ),
          print(f'│ Start Time {startTime} End Time {endTime}',file=resultFile ),
          print(f'│ Run Time seconds {endTime - startTime}',file=resultFile ),
          print(f'├──────────────────────────────────────────────────────────────────────────',file=resultFile ),
          print(f'│ By Bernkra                Git https://github.com/Bernkra96/fibonacci-py  ',file=resultFile )
          print(f'└──────────────────────────────────────────────────────────────────────────',file=resultFile  )
          
          
          resultFile.close
     elif  runFor == 0 or inputVal is None: 
          print(f'Error No Run. "Run for N" to wars Set to 0.')
   
         
     


         


def options():
     print("Options") 
     print("e for exit,h for help,i for info,u for update") 
    
     while True:
          inputVal = input("Text(Listed Only).: ")
          
          if any(char.lower() == 'e' for char in inputVal):
               setup()
               break
          elif  any(char.lower() == 'h' for char in inputVal):
               print('Help')  
               print('o = Options')  
               print('Opens Options ')
               print('e = Exit ')  
               print('Exit Options ')  
               print('u = Exit ')  
               print(f'Update Options')    
               
          elif  any(char.lower() == 'i' for char in inputVal):
               print('Info')  
               print(optionsDataSet) 
               
          elif  any(char.lower() == 'u' for char in inputVal):
               print('Update')  
               updaterOptions() 
               break    
          else :

             print("Is not Valid ")     
          
          

def updaterOptions():
     while True:
               
     
          print("Update witch Option ?")
          print(optionsDataSet) 
          print("Put Option Name in or e for exit") 

          selectOptionsUserInput = input("Text(Option Name).: ")

         
          if selectOptionsUserInput in optionsDataSet:
               updateSetting(optionsDataSet,selectOptionsUserInput)
               break
          elif any(char.lower() == 'e' for char in selectOptionsUserInput):
               options()
               break
          else: 
           print("No Valet input")
          

        
def updateSetting(name , keyData ):    
     
     key = keyData
     
     while True:
          
     
          match name[key]:
               case bool():
                    print("Is a Bool Stetting")
                    print(f'Name of Setting {key} and is, {name[key]}')
                    
                    forBoolInput = input("Type true or false.: ")
                    if forBoolInput == 'true':
                      optionsDataSet[key] = True
                      print(f"Set to { optionsDataSet[key]}")
                      
                      break
                    
                    elif forBoolInput == 'false':
                         optionsDataSet[key] = False
                         print(f"Set to { optionsDataSet[key]}")
 
                         break
              
                    else: 
                         print("No Valet input") 
                         
           
               
          
                
              
                        
              
               case int():
                    print("Is Int Setting")
                    print(f'Name of Setting {key} and is, {name[key]}')
                    forIntInput = input("Type Number.: ")
                    
                    if any(char.isdigit() for char in forIntInput) is True:
                           optionsDataSet[key] = int(forIntInput)
                           print(f"Set to { optionsDataSet[key]}")
                           break
                    else: 
                         print("No Valet input") 
                         
               case _:
                    print("Error No Valid Format ")

     options()        
 
     


setup()
calc()    
printResult()
#EndTimer
if optionsDataSet["EndTimer"] == True :
     time.sleep(optionsDataSet["TimeEndTimer"])