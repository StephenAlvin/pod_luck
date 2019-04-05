#IMPORTING THE LIBRARIES

import RPi.GPIO as GPIO
from gpiozero import DistanceSensor
from time import sleep
from libdw import pyrebase

#SETTING UP FIREBASE

url = 'https://podluck-b3df6.firebaseio.com/'
apikey = 'AIzaSyAO161UH-GGDD0ZzVjqtL-OkginRAM_uRI'
config = {"apiKey": apikey,"databaseURL": url,}
firebase = pyrebase.initialize_app(config)
db = firebase.database()
occupancy = ["initial"]

#SETTING UP THE SERVO

GPIO.setmode(GPIO.BCM) #Use the BCM GPIO numbering scheme.
GPIO.setup(14, GPIO.OUT) #SERVO PIN
#GPIO.setup(12, GPIO.OUT) #POWER PIN
p = GPIO.PWM(14, 50)#PWM of 50Hz

#CREATING FUNCTIONS FOR TURNING SERVOS & SENDING DATA TO FIREBASE

def occupied():
    #GPIO.output(12, 1)
    p.start(2.5)
    p.ChangeDutyCycle(12.5) # turn towards 180 degree
    sleep(1) # sleep 1 second
    occupancy[0] = "occupied"
    db.child("r_pi").set(occupancy)
    print("occupied!")
    #GPIO.output(12, 0)
    
def not_occupied():
    #GPIO.output(12, 1)
    p.start(2.5)
    p.ChangeDutyCycle(2.5) # turn towards 180 degree
    sleep(1) # sleep 1 second
    occupancy[0] = "not_occupied"
    db.child("r_pi").set(occupancy)
    print("not occupied!")
    #GPIO.output(12, 0)

#SETTING UP THE SENSOR
ultrasonic = DistanceSensor(echo=24, trigger=23, threshold_distance=0.4)

#CODE THAT RUNS
#p.start(2.5) #initialize servo

while True:
        ultrasonic.wait_for_in_range()
        occupied()
        ultrasonic.wait_for_out_of_range()
        not_occupied()
