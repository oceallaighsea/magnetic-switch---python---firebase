# Firebase Database URL
# https://lccsproject2022-default-rtdb.europe-west1.firebasedatabase.app/
# Get the url as shown above for your database, check the guide.
# Created new database on 15-12... will need to be replaced in 30 days from then

# Purpose of this program is to connect to a microbit via serial link/usb connection
# The microbit will send information depending magnetic reading.
# The microbit will send a 1 if the magnetic force drops below 100 otherwise a 0

# when the data is recieved it will be cleaned and then sent to the database
# A timestamp will also be created and sent to db as this can be used for a lot of things.

import serial
import time
import datetime

from firebase import firebase

myDBConn = firebase.FirebaseApplication('https://lccsproject2022-default-rtdb.europe-west1.firebasedatabase.app/', None)

serCon = serial.Serial()
serCon.baudrate = 115200
serCon.port = "COM18" # This can sometimes change 
serCon.open()
print("SUCCESS WE HAVE GOT THIS FAR ")

while True:
    microbitData = str(serCon.readline())
    #print(microbitData)
    door = microbitData[2:] # slice string from pos 3 to the end of the string
    #Remove spaces from the string
    door = door.replace(" ","")
    #Replace the escape characters with an empty char using the replace function()
    door = door.replace("\\r\\n","")
    #replace the ' character with ""
    door = door.replace("'","")
    #convert the string to an int
    door = int(door)
    
    print("The Door is open if this value is 1:- ",door)
    print("Use appropriate if statements to carry out required tasks..")
    

    #now = datetime.datetime.now()
    
    now = int(datetime.datetime.today().strftime("%Y%m%d%H%M%S"))# %Y%m%d%H%M%S formats year month day hour min sec
    print(now)
    if door == 1:
        doorOpen = "Open"
    else:
        doorOpen = "Closed"
        
    record = {
     "magnet" : doorOpen,
     "timeStamp" : now 
    }

    result = myDBConn.post("magneticSwitch", record)
    #print the unique id that is returned from the firebase database
    print(result)
    
    time.sleep(5)
 
serCon.close()
myDBCon.close()
    

