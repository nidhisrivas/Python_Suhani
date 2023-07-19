
import datetime

dreamCar = {
           "Make" : "Tesla",
           "Model" : "Y",
           "Year" : "2023",
           "Color" : "White",
           "Auto Transmission" : True,
           "Pre_Owned" : True,
           "Cost" : "68000"
          }

year = datetime.datetime.today().year

if(dreamCar["Pre_Owned"]):
    if(int(dreamCar["Year"]) < int(year - 5)):
       (dreamCar["Cost"]) = int(dreamCar["Cost"]) - int(dreamCar["Cost"]) * .4
    elif(int(dreamCar["Year"]) < int(year - 10)):
        (dreamCar["Cost"]) = int(dreamCar["Cost"]) - int(dreamCar["Cost"]) * .6
    elif(int(dreamCar["Year"])) < int(year -10):
         (dreamCar["Cost"]) = int(dreamCar["Cost"]) - int(dreamCar["Cost"]) * .85

if(dreamCar["Auto Transmission"]):
    (dreamCar["Cost"]) = int(dreamCar["Cost"]) + 2000
    
for key in dreamCar:
    print(key, '->', dreamCar[key])



    
      
         
    
    

