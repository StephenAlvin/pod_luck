#IMPORTING THE LIBRARIES
import RPi.GPIO as GPIO
from time import sleep
from libdw import pyrebase

#SETTING UP FIREBASE
url = 'https://podluck-b3df6.firebaseio.com/'
apikey = 'AIzaSyAO161UH-GGDD0ZzVjqtL-OkginRAM_uRI'
config = {"apiKey": apikey,"databaseURL": url,}
firebase = pyrebase.initialize_app(config)
db = firebase.database()
#root = db.child("/").get()
var = db.child("r_pi").get()
occupancy_list = var.val()
pod0_occupancy = occupancy_list[0]

#SETTING UP THE SERVO
GPIO.setmode(GPIO.BCM) #Use the BCM GPIO numbering scheme.
GPIO.setup(14, GPIO.OUT) #SERVO PIN
p = GPIO.PWM(14, 50)#PWM of 50Hz

#CREATING FUNCTIONS FOR TURNING SERVOS & SENDING DATA TO FIREBASE
def occupied():
    p.start(2.5)
    p.ChangeDutyCycle(6.7) # turn towards 180 degree
    sleep(1) # sleep 1 second
    print(pod0_occupancy)
def not_occupied():
    p.start(2.5)
    p.ChangeDutyCycle(2.5) # turn towards 180 degree
    sleep(1) # sleep 1 second
    print(pod0_occupancy)

#CODE THAT RUNS
while True:
    var = db.child("r_pi").get()
    occupancy_list = var.val()
    pod0_occupancy = occupancy_list[0]
    if pod0_occupancy == 'occupied':
        occupied()
    if pod0_occupancy == 'not_occupied':
        not_occupied()



