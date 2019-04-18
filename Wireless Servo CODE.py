#IMPORTING THE LIBRARIES
import RPi.GPIO as GPIO
from time import sleep
from libdw import pyrebase

#SETTING UP FIREBASE
url = 'https://podluck-b3df6.firebaseio.com/'
apikey = 'AIzaSyAO161UH-GGDD0ZzVjqtL-OkginRAM_uRI'
config = {"apiKey": apikey,"databaseURL": url,}
firebase = pyrebase.initialize_app(config)
db = firebase.database()           # create a databse called db
var = db.child("r_pi").get()       # .get() the .child of "r_pi" from the database db
                                   # var = {'r_pi' : ['occupied', not_occupied', 'not_occupied'........
occupancy_list = var.val()         # opens up the dict and pulls out the values from the dict, .i.e one list that goes by ['occupied', not_occupied', 'not_occupied'........
print(occupancy_list)              # occupancy_list = ['occupied', not_occupied', 'not_occupied'........
pod0_occupancy = occupancy_list[0] # calls the first value from occupancy list

#SETTING UP THE SERVO
GPIO.setmode(GPIO.BCM)   # Use the BCM GPIO numbering scheme.
GPIO.setup(18, GPIO.OUT) # set pin18 as the SERVO PIN
p = GPIO.PWM(18, 50)     # Set a PWM of 50Hz out of pin18


#CREATING FUNCTIONS FOR TURN ING SERVOS & SENDING DATA TO FIREBASE
def occupied():
    #p.start(2.5) #whatever angular displacement the servo horn is at, it will go back to position at 2.5
    p.ChangeDutyCycle(6.7) # turn towards 180 degree
    sleep(1) # sleep 1 second
    print(pod0_occupancy)
def not_occupied():
    #p.start(2.5)
    p.ChangeDutyCycle(2.5) # turn towards 180 degree
    sleep(1) # sleep 1 second
    print(pod0_occupancy)

#CODE THAT
    
p.start(2.5) #swing the servo horn to the initial position regardless which angle it is

while True:
    
    var = db.child("r_pi").get() 
    occupancy_list = var.val()
    pod0_occupancy = occupancy_list[0]
    
    #run conditional loop to determine if pod occupied
    
    if pod0_occupancy == 'occupied':          #check if pod occupancy function gives occupied value
        occupied()                            #run occupied function
    if pod0_occupancy == 'not_occupied':      #if pod occupancy function gives unoccupied
        not_occupied()                        #run unoccupied function



