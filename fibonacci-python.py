"""Fibonacci sequence"""


import json
import os
import sys
import time

# Options preset #"":{"val": "" ,"infoShort":""}

optionsDataPreset = {"EndTimer": { "val": True,"infoShort":" Want to Run End timer?"},"TimeEndTimer":  { "val": 2, "infoShort":"Set EndTimer Length in sek."} , "PrintEndResult" : { "val":  True ,"infoShort":"Print Result in Console" }, "SaveEndResult" : {"val" : True, "infoShort":"Save Result as in Text File "} , "startValA":{"val": 0 ,"infoShort":"Start Val A"},"startValB":{"val": 1 ,"infoShort":"Start Val B"}, "PresetNumberRuns":{"val": 1000 ,"infoShort":"Number of Run if preset if no input "}  }

#Limit for int to string conversion

limString = 0 #set limit for int to string conversion // 0 for unlimited
sys.set_int_max_str_digits(limString)


def optionsLoader():
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
     
     
def optionsSaver(data): # Save Data to File

     global optionsDataSet
     with open("options.json", "w") as optionsDataSetFile:
          json.dump(data,optionsDataSetFile)
     optionsDataSetFile.close
def setup(): # Setup for run. Arks for N Target and opens Options 
   

     global runFor
     global inputVal
     print('─────────────────────────────────────────────────────────'),
     print('Hallo Welcome.')
     print('To this Fibonacci Runner / Benchmark.')
     print('Set Number off runs.')
     print("press ender for preset , o for options, s for set up , q for quit ")

     while True:
          inputVal = input("Number or Text (Listed Only).: ")
     
    
          if any(char.isdigit() for char in inputVal):
               print("Is Valid InT.") 
               inputVal = int(inputVal)
           
               runFor = inputVal
               print(f'Runs Fibonacci.Set for {runFor} times.')
               break
           
          elif any(char.lower() == 'o' for char in inputVal):

               options()    
               break 
          elif any(char.lower() == 's' for char in inputVal):
           
            print("Update witch Option ?")
         
            for i in range(int(len(optionsDataSet))):
               key = list(optionsDataSet.keys())[i]
               print(f"DataName {key} │  DataValue {optionsDataSet[key]["val"]} │  Info: {optionsDataSet[key]["infoShort"]}")  
   
            setup() 
            break 
          
          elif  any(char.lower() == 'q' for char in inputVal):
               print('Quit') 
               sys.exit()
               break
           
          else :

               print("Is not Valid InT or Text.")     
               print("Run Prest Int.") 
               inputVal = int(optionsDataSet["PresetNumberRuns"]["val"])
           
               runFor = inputVal
               print(f'Runs Fibonacci.Set for {runFor} times.')
               break
           
          
def calc(a ,b):  #Runs  Fibonacci calc


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
          B = A
          A = C


     endTime = time.time()  #END Time 
 
 


def printResult(): # Result Printer in Terminal ans result File 
     
     if 'i' in globals() and optionsDataSet["PrintEndResult"]["val"] or 'i' in locals() and optionsDataSet["PrintEndResult"]["val"]:
        

          print(f'┌─────────────────────────────────────────────────────────'),
          print(f'│ Set Number of Runs: {runFor}'),
          print(f'│ Run Number of Runs: {i+1}'),
          print(f'├─────────────────────────────────────────────────────────'),
          print(f'│ Start Time {startTime} End Time {endTime}'),
          print(f'│ Run Time seconds {endTime - startTime}'),
          print(f'└─────────────────────────────────────────────────────────')

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
     print("Options") 
     print("e for exit,h for help,i for info,u for update") 
    
     while True:
          inputVal = input("Text (Listed Only).: ")
          
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
               print("Update witch Option ?")
         
               for i in range(int(len(optionsDataSet))):
                    key = list(optionsDataSet.keys())[i]
                    print(f"DataName {key} │  DataValue {optionsDataSet[key]["val"]} │  Info: {optionsDataSet[key]["infoShort"]}") 
               
          elif  any(char.lower() == 'u' for char in inputVal):
               print('Update')  
               updaterOptions() 
               break 
           
          else :

             print("Is not Valid ")     
          
          
def updaterOptions(): # options Update Selector 
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
           print("No Valet input")
          

        
def updateSetting(name , keyData ): # Option Update function 
     
     key = keyData
     
     while True:
          
     
          match name[key]["val"]:
               
               case bool():
                    print("Is a Bool Stetting")
                    print(f'Name of Setting {key} and is, {name[key]["val"]}  | Info {name[key]["infoShort"]} ')
                    
                    forBoolInput = input("Type true or false.: ")
                    if forBoolInput == 'true':
                         optionsDataSet[key]["val"] = True
                         print(f"Set to { optionsDataSet[key]["val"]}")
                         optionsSaver(optionsDataSet)
                         break
                    
                    elif forBoolInput == 'false':
                         optionsDataSet[key]["val"] = False
                         print(f"Set to { optionsDataSet[key]["val"]}")
                         optionsSaver(optionsDataSet)
                         break
              
                    else: 
                         print("No Valet input") 
                         
           
               case int():
                    print("Is Int Setting")
                    print(f'Name of Setting {key} and is, {name[key]["val"]}')
                    forIntInput = input("Type Number.: ")
                    
                    if any(char.isdigit() for char in forIntInput):
                         optionsDataSet[key]["val"] = int(forIntInput)
                         print(f"Set to { optionsDataSet[key]["val"]}")
                         optionsSaver(optionsDataSet)
                         break
                    else: 
                         print("No Valet input") 
                         
               case _:
                    print("Error No Valid Format ")
     
   
     options()        
 

optionsLoader()  
setup()
calc(optionsDataSet["startValA"]["val"],optionsDataSet["startValB"]["val"])    
printResult()
optionsSaver(optionsDataSet)
#EndTimer
if optionsDataSet["EndTimer"]["val"]:
     time.sleep(optionsDataSet["TimeEndTimer"]["val"])