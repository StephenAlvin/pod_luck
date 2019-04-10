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

#SETTING UP THE SERVO

GPIO.setmode(GPIO.BCM)          #Use the BCM GPIO numbering scheme.
GPIO.setup(14, GPIO.OUT)        #SERVO PIN
#GPIO.setup(12, GPIO.OUT)       #POWER PIN
p = GPIO.PWM(14, 50)            #PWM of 50Hz

#CREATING FUNCTIONS FOR TURNING SERVOS & SENDING DATA TO FIREBASE

def occupied():
    p.start(2.5)
    p.ChangeDutyCycle(12.5)                     # turn towards 180 degree
    sleep(1)                                    # sleep 1 second
    db.child("r_pi").update({"0":"occupied"})
    print("occupied!")
    
def not_occupied():
    p.start(2.5)
    p.ChangeDutyCycle(2.5) # turn towards 180 degree
    sleep(1) # sleep 1 second
    db.child("r_pi").update({"0":"not_occupied"})
    print("not occupied!")

#SETTING UP THE SENSOR
ultrasonic = DistanceSensor(echo=24, trigger=23, threshold_distance=0.4)

while True:
        ultrasonic.wait_for_in_range()
        occupied()
        ultrasonic.wait_for_out_of_range()
        not_occupied()
