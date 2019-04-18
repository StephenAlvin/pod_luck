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

                                #SETTING UP THE SERVO
GPIO.setmode(GPIO.BCM)             # Use the BCM GPIO numbering scheme.
GPIO.setup(18, GPIO.OUT)           # set pin18 as the SERVO PIN
p = GPIO.PWM(18, 50)               # Set a PWM of 50Hz out of pin18

                                #CREATING FUNCTIONS FOR TURN ING SERVOS & SENDING DATA TO FIREBASE
def occupied():                    # function for if pod is occupied
    p.ChangeDutyCycle(6.7)         # turn towards 180 degree
    sleep(1)                       # sleep 1 second
    print(pod0_occupancy)          # print occupancy
def not_occupied():                # function for if pod is occupied
    p.ChangeDutyCycle(2.5)         # turn towards 180 degree
    sleep(1)                       # sleep 1 second
    print(pod0_occupancy)          # print occupancy

                                #CODE THAT ACTUALLY RUNS  
p.start(2.5)                       # swing the servo horn to the initial position regardless which angle it is
while True:
    occupancy_list = db.child("r_pi").get().val()         # occupancy_list = ['occupied', not_occupied', 'not_occupied'.......
    pod0_occupancy = occupancy_list[0]                    # store the occupancy for the first pod : pod0
                                                          #run conditional loop to determine if pod occupied
    if pod0_occupancy == 'occupied':          #check if pod occupancy function gives occupied value
        occupied()                            #call occupied function
    if pod0_occupancy == 'not_occupied':      #if pod occupancy function gives unoccupied
        not_occupied()                        #call unoccupied function



