#IMPORTING THE LIBRARIES

import RPi.GPIO as GPIO
from gpiozero import DistanceSensor
from libdw import pyrebase

#SETTING UP FIREBASE

url = 'https://podluck-b3df6.firebaseio.com/'
apikey = 'AIzaSyAO161UH-GGDD0ZzVjqtL-OkginRAM_uRI'
config = {"apiKey": apikey,"databaseURL": url,}
firebase = pyrebase.initialize_app(config)
db = firebase.database()

#CREATING FUNCTIONS FOR SENDING DATA TO FIREBASE

def occupied():
    db.child("r_pi").update({"0":"occupied"})
    print("occupied!")
    
def not_occupied():
    db.child("r_pi").update({"0":"not_occupied"})
    print("not occupied!")

#SETTING UP THE SENSOR

ultrasonic = DistanceSensor(echo=24, trigger=23, threshold_distance=0.4)


#CODE THAT RUNS

while True:
        ultrasonic.wait_for_in_range()
        occupied()
        ultrasonic.wait_for_out_of_range()
        not_occupied()

