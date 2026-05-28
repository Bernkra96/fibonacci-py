"""Fibonacci sequence"""

import typing
import json
import os
import sys
import time
import warnings

# Options preset #"":{"val": "" ,"infoShort":""}

optionsDataPreset = {"EndTimer": { "val": True,"infoShort":" Want to Run End timer?"},"TimeEndTimer":  { "val": 2, "infoShort":"Set EndTimer Length in sek."} , "PrintEndResult" : { "val":  True ,"infoShort":"Print Result in Console" }, "SaveEndResult" : {"val" : True, "infoShort":"Save Result as in Text File "} , "startValA":{"val": 0 ,"infoShort":"Start Val A"},"startValB":{"val": 1 ,"infoShort":"Start Val B"}, "PresetNumberRuns":{"val": 1000 ,"infoShort":"Number of Run if preset if no input "}  }

#Limit for int to string conversion

limString = 0 #set limit for int to string conversion // 0 for unlimited
sys.set_int_max_str_digits(limString)


def optionsLoader():
     """ Load Options file or make new if not three   
     """
     global optionsDataSet

     with open("options.json", "a") as  optionsDataSetFile: # Check if file has data if not Load preset 
          if os.path.getsize('options.json') == 0:
               print("options Empty")
               json.dump(optionsDataPreset,optionsDataSetFile)
          
    
     with open("options.json", "r+") as optionsDataSetFile:   
         
          optionsDataSet = json.load(optionsDataSetFile) # Load options 
          if len(optionsDataSet.keys()) != len(optionsDataPreset.keys()): #Fix options if missing keys and Load preset
               optionsDataSetFile.seek(0)
               json.dump(optionsDataPreset,optionsDataSetFile)
               optionsDataSetFile.truncate() 
               optionsDataSet = json.load(optionsDataSetFile)  # Load options 
          
          optionsDataSetFile.close
     
     
def optionsSaver(data: dict): # Save Data to File
     """Save data to File 

     Args:
         data (dict): Python dictionary
     """

     global optionsDataSet
     with open("options.json", "w") as optionsDataSetFile:
          json.dump(data,optionsDataSetFile)
     optionsDataSetFile.close

def setup(): # Setup for run. Arks for N Target and opens Options 
     """ 
     Setup for run. Arks for N Target and opens Options 

          runFor : Number of Nuns 
          inputVal : user input Number of Runs or string for options select  
     """

     global runFor
     global inputVal
     print('─────────────────────────────────────────────────────────'),
     print('Hallo Welcome.')
     print('To this Fibonacci Runner / Benchmark.')
     print('Set Number off runs.')
     print("press ender for preset , o for options, s for set up , q for quit ")

     while True:
          inputVal = input("Number or Text (Listed Only).: ")
     
    
          if any(char.isdigit() for char in inputVal):  #Run with input if Num . Break Loop to lode next calc Functions 
               inputVal = int(inputVal)
           
               runFor = inputVal
               print(f'Runs Fibonacci.Set for {runFor} times.')
               break
           
          elif any(char.lower() == 'o' for char in inputVal): # Lode options 

               options()    
               break 
          elif any(char.lower() == 's' for char in inputVal): # Lode Setup 
           
            print("Update witch Option ?")
         
            for i in range(int(len(optionsDataSet))):
               key = list(optionsDataSet.keys())[i]
               print(f"DataName {key} │  DataValue {optionsDataSet[key]["val"]} │  Info: {optionsDataSet[key]["infoShort"]}")  
   
            setup() 
            break 
          
          elif  any(char.lower() == 'q' for char in inputVal):   # Close Program 
               print('Quit') 
               sys.exit()
               break
           
          else :     #Run with PreSetNum if no valid input. Break Loop to lode next calc Functions 
               
               print("Is not Valid InT or Text.")     
               print("Run Prest Int.") 
               inputVal = int(optionsDataSet["PresetNumberRuns"]["val"])
           
               runFor = inputVal
               print(f'Runs Fibonacci.Set for {runFor} times.')
               break
           
          
def calc(a: int ,b: int , runFor: int)  -> None :  #Runs  Fibonacci calc
     """Calcs  Fibonacci for runFor Val  

     Args:
         a (int): fist int starts with 0 from startValA options
         b (int): fist int starts with 1 from startValB options
         runFor(int): number of runs 
     """

     global A 
     global B
     global i
     global startTime
     global endTime
           
     A = a
     B = b


     startTime = time.time() #Start Time 
    
     for  i in range(runFor):
     
          C = A + B
       
          print(C)
          A = B
          B = C
        


     endTime = time.time()  #END Time 
 
 


def printResult(): # Result Printer in Terminal and result File 
     ''' Result Printer in Terminal And Text File  or error if no run  
     '''

     
     if 'i' in globals() and optionsDataSet["PrintEndResult"]["val"] or 'i' in locals() and optionsDataSet["PrintEndResult"]["val"]:
        
          print(f'┌──────────────────────────────────────────────────────────────────────────'),
          print(f'│ Fibonacci Runner / Benchmark Result')
          print(f'├──────────────────────────────────────────────────────────────────────────'), 
          print(f'│ Set Number of Runs: {runFor}'),
          print(f'│ Run Number of Runs: {i+1}'),
          print(f'├──────────────────────────────────────────────────────────────────────────'),
          print(f'│ Start Time {startTime} End Time {endTime}'),
          print(f'│ Run Time seconds {endTime - startTime}'),
          print(f'├──────────────────────────────────────────────────────────────────────────'),
          print(f'│ By Bernkra                Git https://github.com/Bernkra96/fibonacci-py  '),
          print(f'└──────────────────────────────────────────────────────────────────────────')
          

     elif  runFor == 0 or inputVal is None: 
          
          print(f'Error No Run. "Run for N" to wars Set to 0.') 
   
     if 'i' in globals() and optionsDataSet["SaveEndResult"]["val"] or 'i' in locals() and optionsDataSet["SaveEndResult"]["val"]:
         with  open("result.txt", "w",encoding='utf-8') as resultFile :
         
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
          print(f'└──────────────────────────────────────────────────────────────────────────',file=resultFile )
          
          
          resultFile.close
    
     elif  runFor == 0 or inputVal is None: 
       
          print(f'Error No Run. "Run for N" to wars Set to 0.')


def options(): # options View 
     """Options  Select and Show

      inputVal : user input Number of Runs or string for options select
     """
     print("Options") 
     print("e for exit,h for help,i for info,u for update") 
    
     while True:
          inputVal = input("Text (Listed Only).: ")
          
          if any(char.lower() == 'e' for char in inputVal): # Lode setup
               setup()
               break
          elif  any(char.lower() == 'h' for char in inputVal): # Show help
               print('Help')  
               print('o = Options')  
               print('Opens Options ')
               print('e = Exit ')  
               print('Exit Options ')  
               print('u = Exit ')  
               print(f'Update Options')    
               
          elif  any(char.lower() == 'i' for char in inputVal): # Show Info and options data
               print('Info')  
               print("Update witch Option ?")
         
               for i in range(int(len(optionsDataSet))):
                    key = list(optionsDataSet.keys())[i]
                    print(f"DataName {key} │  DataValue {optionsDataSet[key]["val"]} │  Info: {optionsDataSet[key]["infoShort"]}") 
               
          elif  any(char.lower() == 'u' for char in inputVal): # Lode updaterForOptions
               print('Update')  
               updaterOptions() 
               break 
           
          else :

              warnings.warn("No Valet input")  
          
          
def updaterOptions(): # options Update Selector 
     """options Update Selector 


     Select option to Update mach input st key 

     Raises:
         ValueError: If None is Given 
     """
     while True:
               
     
          print("Update witch Option ?")
         
          for i in range(int(len(optionsDataSet))):
               key = list(optionsDataSet.keys())[i]
               print(f"DataName {key} │  DataValue {optionsDataSet[key]["val"]} │  Info: {optionsDataSet[key]["infoShort"]}")

          print("Put Option Name in or e for exit")

          selectOptionsUserInput = input("Text (Option Name).: ")

         
          if selectOptionsUserInput in optionsDataSet:
               updateSetting(optionsDataSet,selectOptionsUserInput)
               break
          elif any(char.lower() == 'e' for char in selectOptionsUserInput):
               options()
               break
          else: 
               raise ValueError("No valid input ")

          

        
def updateSetting(name :dict, keyData :str): # Option Update function 
     """Update Option val with input Checking 

     Args:
         name (dict): Data sets Python dictionary
         keyData (str): Key 
     """
     key = keyData
     
     while True:
          
     
          match name[key]["val"]: # Mach val type 
               
               case bool(): #Update Bool
                    print("Is a Bool Stetting")
                    print(f'Name of Setting {key} and is, {name[key]["val"]}  | Info {name[key]["infoShort"]} ')
                    
                    forBoolInput = input("Type true or false.: ")
                   
                    if forBoolInput.lower() == 'true':
                         optionsDataSet[key]["val"] = True
                         print(f"Set to { optionsDataSet[key]["val"]}")
                         optionsSaver(optionsDataSet)
                         break
                    
                    elif forBoolInput.lower() == 'false':
                         optionsDataSet[key]["val"] = False
                         print(f"Set to { optionsDataSet[key]["val"]}")
                         optionsSaver(optionsDataSet)
                         break
              
                    else: 
                         
                         warnings.warn("No Valet input")
                         
           
               case int():  #Update int
                    print("Is Int Setting")
                    print(f'Name of Setting {key} and is, {name[key]["val"]}')
                    forIntInput = input("Type Number.: ")
                    
                    if any(char.isdigit() for char in forIntInput):
                         optionsDataSet[key]["val"] = int(forIntInput)
                         print(f"Set to { optionsDataSet[key]["val"]}")
                         optionsSaver(optionsDataSet)
                         break
                    else: 
                          warnings.warn("No Valet input")
                         
               case _:
                     raise ValueError("No valid input ")
     
   
     options()        
 



if __name__ == "__main__":   # Main warper git
     optionsLoader()  
     setup()
     calc(optionsDataSet["startValA"]["val"],optionsDataSet["startValB"]["val"],runFor )    
     printResult()
     optionsSaver(optionsDataSet)
     #EndTimer
     if optionsDataSet["EndTimer"]["val"]:
          time.sleep(optionsDataSet["TimeEndTimer"]["val"])